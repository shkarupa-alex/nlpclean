from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='nlpclean',
    version='1.0.2',
    description='Utilities for cleaning up text corpus',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shkarupa-alex/nlpclean',
    author='Shkarupa Alex',
    author_email='shkarupa.alex@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'newspaper3k>=0.2.8',
        'beautifulsoup4>=4.8.2',
        'langid>=1.1.6',
        'pycld2>=0.41',
        'pyfasttext>=0.4.6',
        'tqdm>=4.45.0'
    ],
    python_requires='>=3.6.0',
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
