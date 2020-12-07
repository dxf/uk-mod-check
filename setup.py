#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
      name='uk-mod-check',
      version='1.0',
      author='Q 🦄',
      author_email='q@magicalcodewit.ch',
      packages=find_packages(),
      include_package_data=True,
      package_data={
            '': ['data/*.txt']
      },
)
