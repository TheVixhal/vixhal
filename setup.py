from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'A library designed for secure key-value storage using AES encryption. It provides functionality for generating AES keys, encrypting and decrypting data, and converting between text and bytes. The library is designed for in-memory storage, making it suitable for fast, temporary data handling.'
LONG_DESCRIPTION = open("README.md").read()

# Setting up
setup(
    name="vixhal",
    version=VERSION,
    author="Vishal Singh Baraiya",
    author_email="<thevishal010@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pycryptodome'],
    keywords=['python', 'vixhal', 'encrypt', 'decrypt', 'bytes', 'AES', 'store', 'retrieve', 'generate key', 'secure'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ], 
    test_suit = "tests"
)