#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='eagerplayer',
      version='0.0.1',
      description='Python module demonstrating use cases',
      author='Ondrej Platek',
      author_email='oplatek@oplatai.com',
      packages=find_packages(),
      url='https://github.com/oplatek/tf-eager-playground',
      install_requires=[
          # TODO fails 'tensorflow>=1.12',
          'numpy>=1.15.3',
          ],
      tests_require=[],
     )
