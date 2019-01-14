#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ronen Lapushner'
SITENAME = 'Ronen Lapushner'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = 'pelican-themes/pelican-blue'

# Social widget
SOCIAL = (
        ('linkedin', 'https://www.linkedin.com/in/ronen-lapushner-521966143/'),
        ('github', 'https://github.com/ronen25/'),
        ('facebook', 'https://www.facebook.com/ronen.lapushner')
        )

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static paths
STATIC_PATHS = ['cv_files', 'screenshots', 'pictures']
