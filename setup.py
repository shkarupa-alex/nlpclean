from pathlib import Path

from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='nlpclean',
    version='1.0.6',
    description='Utilities for cleaning up text corpus',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shkarupa-alex/nlpclean',
    author='Shkarupa Alex',
    author_email='shkarupa.alex@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=Path("requirements.txt").read_text().splitlines(),
    # dependency_links=[
    #     # TODO: remove when newspaper3k dependency will be updated
    #     'https://github.com/fxsjy/jieba/tarball/jieba3k#egg=jieba3k-0.35.1'
    # ],
    python_requires='>=3.7.0',
    # setup_requires=["pytest-runner"],
    # tests_require=["pytest"],
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
