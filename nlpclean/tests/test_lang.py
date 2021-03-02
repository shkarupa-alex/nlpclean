import os
import unittest
from ..lang import detect_main_lang


class TestDetectMainLang(unittest.TestCase):
    def test_unknown(self):
        lang, reliable, score = detect_main_lang('')

        self.assertEqual(lang, 'en')
        self.assertEqual(reliable, False)
        self.assertAlmostEqual(score, 0.06997770129373095, places=5)

    def test_short(self):
        lang, reliable, score = detect_main_lang('Привет')

        self.assertEqual(lang, 'ru')
        self.assertEqual(reliable, False)
        self.assertAlmostEqual(score, 0.3783611307416391, places=5)

    def test_english(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'english.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'en')
        self.assertEqual(reliable, True)
        self.assertAlmostEqual(score, 0.9925090072061524, places=5)

    def test_russian(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'russian.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'ru')
        self.assertEqual(reliable, True)
        self.assertAlmostEqual(score, 0.8938933546983399, places=5)

    def test_bulgarian(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'bulgarian.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'bg')
        self.assertEqual(reliable, True)
        self.assertAlmostEqual(score, 0.9437685205484885, places=5)

    def test_ukrain(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'ukrain.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'uk')
        self.assertEqual(reliable, True)
        self.assertAlmostEqual(score, 0.979860581573331, places=5)

    def test_combined(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'combined.txt'), 'rt') as f:
            lang, reliable, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'uk')
        self.assertEqual(reliable, False)
        self.assertLess(score, 0.5)
