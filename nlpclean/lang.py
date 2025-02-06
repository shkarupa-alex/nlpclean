import fasttext
import logging
import operator
import os
import requests
import threading
import iso639
import tqdm

_fasttext_model = None
_init_lock = threading.Lock()


def _download_fasttext():
    remote_url = 'https://huggingface.co/cis-lmu/glotlid/resolve/main/model.bin'
    expected_size = 1687094687

    model_dir = os.path.expanduser(os.path.join('~', '.nlpclean'))
    model_dir = os.getenv("DATA_DIR") or model_dir
    os.makedirs(model_dir, exist_ok=True)

    model_name = 'model.bin'
    model_path = os.path.join(model_dir, model_name)

    if os.path.exists(model_path) and os.path.getsize(model_path) == expected_size:
        return model_path

    remote_size = int(requests.head(remote_url, allow_redirects=True).headers['Content-Length'])
    if expected_size != remote_size:
        raise AssertionError('Unexpected remote model size')

    bar = tqdm.tqdm(initial=0, total=remote_size, unit='B', unit_scale=True, desc=model_name)
    req = requests.get(remote_url, allow_redirects=True, stream=True)
    with open(model_path, 'wb') as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                bar.update(1024)
    bar.close()

    return model_path


def detect_main_lang(text):
    if not text.strip():
        return '??', 1.0

    global _fasttext_model
    with _init_lock:
        if _fasttext_model is None:
            _fasttext_model = fasttext.load_model(_download_fasttext())

    try:
        scores = _fasttext_model.predict(text.replace('\n', ' '))
    except Exception as e:
        logging.warning(e)
        return '??', 0.0

    if not scores or not scores[0]:
        return '??', 0.0

    lang = scores[0][0].replace('__label__', '').split('_')[0]
    lang = iso639.Lang(lang).pt1
    if not lang:
        return '??', scores[1][0]

    return lang, scores[1][0]
