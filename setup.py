#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='python-unimus',
      version='0.0.1',
      description='Python Unimus Client',
      long_description=readme(),
      python_requires='>=3',
      author='Michael Rhone',
      author_email='michael@rhone.dev',
      url='https://github.com/Twooey/python-unimus',
      download_url='https://github.com/twooey/python-unimus/releases/tag/0.0.11.tar.gz',
      packages=find_packages(),
      install_requires=['ipaddress', 'requests'],
      classifiers = [
        "Programming Language :: Python :: 3",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
      ],
     )