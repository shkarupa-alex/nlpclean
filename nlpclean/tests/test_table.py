import os
import unittest
from absl.testing import parameterized
from nlpclean.table import table_span_normalize


class TestTableSpanNormalize(parameterized.TestCase):
    def _get_case(self, name):
        inputs_path = os.path.join(os.path.dirname(__file__), 'table_span_normalize', f'{name}.html')
        with open(inputs_path, 'rt') as f:
            inputs = f.read()

        expected_path = inputs_path.replace('.html', '_.html')
        if not os.path.exists(expected_path):
            open(expected_path, 'wt').close()
        with open(expected_path, 'rt') as f:
            expected = f.read()

        return inputs, expected

    @parameterized.parameters(['deep', 'empty', 'iv', 'order', 'row1', 'row2', 'rowcol1', 'rowcol2', 'rowcol3', 'rowcol4', 'rowcol5', 'rowcol6'])
    def test_case(self, name):
        inputs, expected = self._get_case(name)
        result = table_span_normalize(inputs)

        self.assertEqual(expected, result)
