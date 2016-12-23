import os
from setuptools import setup
from setuptools.command.test import test as TestCommand

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "TETRIS",
    version = "1.0.0",
    author = "Vijeth Tumkur Aradhya",
    author_email = "vijthaaa@gmail.com",
    description = ("A simple version of the Tetris Game"),
    license = "BSD",
    keywords = "tetris game curses",
    setup_requires=['pytest-runner', 'pytest'],
    tests_require=['pytest',],
    long_description=read('README'),
)
