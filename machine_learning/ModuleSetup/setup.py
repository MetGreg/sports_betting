#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:41:10 2017

@author: gregor-linux
"""

from setuptools import setup, find_packages
setup(
      name='SportsBettingModule',
      version='0.1.0',
      description='Classes of SportsBetting project',
      long_description='Contains all classes needed for programs of project',
      keywords='sports betting',
      license='GPLv3',
      author='Gregor Möller',
      author_email='gregor_moeller@live.de',
      url='https://github.com/GroovyGregor/sports_betting',
      classifiers=[
              'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
              'Programming Language :: Python :: 3.5',
              'Operating System :: OS Independent',
              'Topic :: Software Development :: Libraries :: Python Modules',
              'Topic :: Utilities'],
      packages=find_packages(),
      install_requires=[
              ]
      )
