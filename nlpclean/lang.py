import operator
import os
import requests
import threading
import tqdm
from langid.langid import LanguageIdentifier, model as langid_model
from pycld2 import detect as cld_detect
from pyfasttext import FastText

_langid_model = None
_fasttext_model = None
_init_lock = threading.Lock()


def _download_fasttext():
    remote_url = 'https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin'
    expected_size = 131266198

    model_dir = os.path.expanduser(os.path.join('~', '.nlpclean'))
    os.makedirs(model_dir, exist_ok=True)

    model_name = 'lid.176.bin'
    model_path = os.path.join(model_dir, model_name)

    if os.path.exists(model_path) and os.path.getsize(model_path) == expected_size:
        return model_path

    remote_size = int(requests.head(remote_url).headers['Content-Length'])
    if expected_size != remote_size:
        raise AssertionError('Unexpected remote model size')

    bar = tqdm.tqdm(initial=0, total=remote_size, unit='B', unit_scale=True, desc=model_name)
    req = requests.get(remote_url, stream=True)
    with open(model_path, 'wb') as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                bar.update(1024)
    bar.close()

    return model_path


def detect_main_lang(text):
    global _langid_model
    with _init_lock:
        if _langid_model is None:
            _langid_model = LanguageIdentifier.from_modelstring(langid_model, norm_probs=True)

    global _fasttext_model
    with _init_lock:
        if _fasttext_model is None:
            _fasttext_model = FastText(_download_fasttext())

    langs = {}
    down = 0.

    try:
        lang, score = _langid_model.classify(text)
        if lang not in langs:
            langs[lang] = 0.
        langs[lang] += score
    except Exception as e:
        print(e)
        down += 0.5

    try:
        _, _, scores = cld_detect(text)
        for _, lang, score, _ in scores:
            if lang not in langs:
                langs[lang] = 0.
            langs[lang] += score / 100
    except Exception as e:
        print(e)
        down += 0.5

    try:
        scores = _fasttext_model.predict_proba([text], 3)[0]
        for lang, score in scores:
            if lang not in langs:
                langs[lang] = 0.
            langs[lang] += score
    except Exception as e:
        print(e)
        down += 0.5

    lang = max(langs.items(), key=operator.itemgetter(1))[0]
    reliable = langs[lang] >= 1.99 - down
    score = langs[lang] / 3.

    return lang, reliable, score