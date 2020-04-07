import os
import unittest
from ..lang import detect_main_lang


class TestDetectMainLang(unittest.TestCase):
    def test_unknown(self):
        lang, reliable, score = detect_main_lang('')

        self.assertEqual(lang, 'en')
        self.assertEqual(reliable, False)
        self.assertEqual(score, 0.056487168652884445)

    def test_short(self):
        lang, reliable, score = detect_main_lang('Привет')

        self.assertEqual(lang, 'ru')
        self.assertEqual(reliable, False)
        self.assertEqual(score, 0.5050400509335103)

    def test_english(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'english.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'en')
        self.assertEqual(reliable, True)
        self.assertEqual(score, 0.9934190876399208)

    def test_russian(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'russian.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'ru')
        self.assertEqual(reliable, True)
        self.assertEqual(score, 0.8567562182014123)

    def test_bulgarian(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'bulgarian.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'bg')
        self.assertEqual(reliable, True)
        self.assertEqual(score, 0.9149695330361064)

    def test_ukrain(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'ukrain.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'uk')
        self.assertEqual(reliable, True)
        self.assertEqual(score, 0.9726822916420593)

    def test_combined(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'combined.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'be')
        self.assertEqual(reliable, False)
        self.assertEqual(score, 0.3933333333333333)
