import os
import unittest
from ..lang import detect_main_lang


class TestDetectMainLang(unittest.TestCase):
    def test_unknown(self):
        lang, reliable, score = detect_main_lang('')

        self.assertEqual(lang, 'en')
        self.assertEqual(reliable, False)
        self.assertEqual(score, 0.0933036017249746)

    def test_short(self):
        lang, reliable, score = detect_main_lang('Привет')

        self.assertEqual(lang, 'ru')
        self.assertEqual(reliable, False)
        self.assertEqual(score, 0.5044815076555188)

    def test_english(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'english.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'en')
        self.assertEqual(reliable, True)
        self.assertEqual(score, 0.9900130995114645)

    def test_russian(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'russian.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'ru')
        self.assertEqual(reliable, True)
        self.assertEqual(score, 0.858525361220042)

    def test_bulgarian(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'bulgarian.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'bg')
        self.assertEqual(reliable, True)
        self.assertEqual(score, 0.9250262475013734)

    def test_ukrain(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'ukrain.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'uk')
        self.assertEqual(reliable, True)
        self.assertEqual(score, 0.9731481417020161)

    def test_combined(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'combined.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'be')
        self.assertEqual(reliable, False)
        self.assertEqual(score, 0.44914431631565094)
