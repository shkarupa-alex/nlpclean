import re
from fastbloom_rs import BloomFilter
from unicodedata import normalize


def dedup_lines_bloom(text, just_words=True, zero_digits=True, capacity=100000000, error=0.00001):
    sbf = BloomFilter(
        expected_elements=capacity,
        false_positive_probability=error
    )

    for line in text:
        if not isinstance(line, str):
            raise TypeError('Expected "text" to contain stings, found: {}'.format(type(line)))

        key = line.strip()
        if not key:
            yield line

        key = normalize('NFKD', key)

        if just_words:
            key = ' '.join(re.findall(r'\w+', key))
        if zero_digits:
            key = re.sub(r'\d', '0', key)

        if key in sbf:
            line = ''
        else:
            sbf.add(key)

        yield line
