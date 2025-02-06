import os
import unittest
from nlpclean.lang import detect_main_lang


class TestDetectMainLang(unittest.TestCase):
    def test_empty(self):
        lang, score = detect_main_lang('')

        self.assertEqual(lang, '??')
        self.assertAlmostEqual(score, 1.0, places=5)

    def test_short(self):
        lang, score = detect_main_lang('Ну')

        self.assertEqual(lang, 'ru')
        self.assertAlmostEqual(score, 0.7732973694801331, places=5)

    def test_nolang(self):
        lang, score = detect_main_lang(
            'ïðàâèëà, ðàçâèòü õîðîøèé ëèòåðàòóðíûé'
            '����+)J���[�����;�U���Q'
        )

        self.assertEqual(lang, '??')
        self.assertAlmostEqual(score, 0.9999790191650391, places=5)

    def test_undetermined(self):
        lang, score = detect_main_lang(
            '𒐰𒔓𒑙𒉜𒀟𒇟𒒻𒂻𒐉𒄉𒀨𒃰𒓴'
            '𞋚 𞋃𞋯𞋣𞋞 𞋰 𞋙𞋮𞋯𞋃𞋆𞋘𞋡𞋸𞋋𞋞𞋟𞋫𞋵'
        )

        self.assertEqual(lang, '??')
        self.assertAlmostEqual(score, 0.9999852180480957, places=5)

    def test_english(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'english.txt'), 'rt') as f:
            lang, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'en')
        self.assertAlmostEqual(score, 0.9848628640174866, places=5)

    def test_russian(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'russian.txt'), 'rt') as f:
            lang, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'ru')
        self.assertAlmostEqual(score, 0.9984455704689026, places=5)

    def test_bulgarian(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'bulgarian.txt'), 'rt') as f:
            lang, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'bg')
        self.assertAlmostEqual(score, 0.9999954700469971, places=5)

    def test_ukrain(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'ukrain.txt'), 'rt') as f:
            lang, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'uk')
        self.assertAlmostEqual(score, 0.9999827146530151, places=5)

    def test_combined(self):
        with open(os.path.join(os.path.dirname(__file__), 'detect_main_lang', 'combined.txt'), 'rt') as f:
            lang, score = detect_main_lang(f.read())

        self.assertEqual(lang, 'uk')
        self.assertAlmostEqual(score, 0.40854740142822266, places=5)
