import gc
import os
import resource
import unittest
from absl.testing import parameterized
from nlpclean.html import html_to_article, fragment_to_markdown, fragment_to_text


class TestHtmlToArticle(parameterized.TestCase):
    def _get_case(self, name):
        inputs_path = os.path.join(os.path.dirname(__file__), 'html_to_markdown', f'{name}.html')
        with open(inputs_path, 'rt') as f:
            inputs = f.read()

        expected_path = inputs_path.replace('.html', '.md')
        if not os.path.exists(expected_path):
            open(expected_path, 'wt').close()
        with open(expected_path, 'rt') as f:
            expected = f.read()

        return inputs, expected

    @parameterized.parameters(['citilink', 'dns', 'drive2', 'gazeta', 'habr', 'iv1', 'iv2', 'iv3', 'iv4', 'iv5', 'kinopoisk', 'kommersant', 'kp', 'lenta', 'livejournal1', 'livejournal2', 'livejournal3', 'mk', 'ozon', 'rbc', 'ria', 'sport', 'vc', 'wb', 'woman', 'zen'])
    def test_makrdown(self, name):
        inputs, expected = self._get_case(name)
        result = html_to_article(inputs)
        result = fragment_to_markdown(result)

        self.assertEqual(expected, result)

class TestFragmentToText(parameterized.TestCase):
    def _get_case(self, name):
        inputs_path = os.path.join(os.path.dirname(__file__), 'fragment_to_text', f'{name}.html')
        with open(inputs_path, 'rt') as f:
            inputs = f.read()

        expected_path = inputs_path.replace('.html', '.txt')
        if not os.path.exists(expected_path):
            open(expected_path, 'wt').close()
        with open(expected_path, 'rt') as f:
            expected = f.read()

        return inputs, expected

    @parameterized.parameters(['article2', 'article3', 'article3', 'article4', 'article4', 'break', 'break', 'comment1', 'comment1', 'comment2', 'comment2', 'empty', 'empty', 'no_space', 'no_space', 'space', 'space'])
    def test_text(self, name):
        inputs, expected = self._get_case(name)
        result = fragment_to_text(inputs)

        self.assertEqual(expected, result)
