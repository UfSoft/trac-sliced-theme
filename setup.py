#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 et

from setuptools import setup

setup(
  name         = 'SlicedTracTheme',
  version      = '1.0',
  packages     = ['slicedtheme'],
  package_data = { 'slicedtheme': [
                    'templates/*.html',
                    'htdocs/*.css',
                    'htdocs/imgs/*.png',
                    'htdocs/imgs/*.gif']},
  author        = 'Pedro Algarvio',
  author_email  = 'ufs@ufsoft.org',
  description   = 'A port of the Sliced theme by , created by http://www.spyka.net',
  license       = 'BSD',
  keywords      = 'sliced trac plugin theme',
  url           = 'https://hg.ufsoft.org/SlicedTracTheme/',
  classifiers   = [
    'Framework :: Trac'
  ],
  install_requires = ['Trac>=0.11', 'TracThemeEngine>=2.0'],
  entry_points = {
    'trac.plugins': [
      'slicedtheme.theme = slicedtheme.theme',
    ]
  },
)
