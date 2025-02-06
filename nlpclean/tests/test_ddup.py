import os
import unittest
from nlpclean.ddup import make_dedup_bloom

# Run this test with PYTHONHASHSEED=0 env
class TestDedupLinesBloom(unittest.TestCase):
    def test_all_dup(self):
        ddp = make_dedup_bloom(just_words=False, zero_digits=False, capacity=10)
        with open(os.path.join(os.path.dirname(__file__), 'dedup_lines_bloom', 'all_dup_source.txt'), 'rt') as f:
            result = ddp(f.read())
        with open(os.path.join(os.path.dirname(__file__), 'dedup_lines_bloom', 'all_dup_ground.txt'), 'rt') as f:
            expected = f.read()

        self.assertEqual(expected, result)

    def test_dup_noise(self):
        ddp = make_dedup_bloom(just_words=True, zero_digits=True, capacity=10)
        with open(os.path.join(os.path.dirname(__file__), 'dedup_lines_bloom', 'dup_noise_source.txt'), 'rt') as f:
            result = ddp(f.read())
        with open(os.path.join(os.path.dirname(__file__), 'dedup_lines_bloom', 'dup_noise_ground.txt'), 'rt') as f:
            expected = f.read()

        self.assertEqual(expected, result)

    def test_some_dup(self):
        ddp = make_dedup_bloom(just_words=True, zero_digits=True, capacity=10)
        with open(os.path.join(os.path.dirname(__file__), 'dedup_lines_bloom', 'some_dup_source.txt'), 'rt') as f:
            result = ddp(f.read())
        with open(os.path.join(os.path.dirname(__file__), 'dedup_lines_bloom', 'some_dup_ground.txt'), 'rt') as f:
            expected = f.read()

        self.assertEqual(expected, result)
