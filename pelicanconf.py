#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ahmed Shibani'
SITENAME = "Shumbashi's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Tripoli'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Libyan Spider', 'https://libyanspider.com/'),
        )

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/ashibani'),
          ('GitHub', 'https://github.com/shumbashi'),
          ('Twitter', 'https://twitter.com/ashibani'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['plugins'] 
PLUGINS = ['i18n_subsites', 'related_posts', 'series']
BOOTSTRAP_THEME = 'flatly'
OUTPUT_PATH = 'docs'
DISPLAY_BREADCRUMBS = True
# DISPLAY_ARTICLE_INFO_ON_INDEX = True
# ABOUT_ME = "I'm Ahmed Shibani"
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARCHIVE_ON_SIDEBAR = True
# DISPLAY_AUTHORS_ON_SIDEBAR = True
CC_LICENSE = "CC-BY"
GITHUB_USER = "shumbashi"
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True
TWITTER_CARDS = True
TWITTER_USERNAME = "a.shibani"
# SHARIFF = True
ADDTHIS_PROFILE = "ra-6072ce1f837f9ede"
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
PYGMENTS_STYLE = "solarizeddark"
CUSTOM_CSS = 'static/css/custom.css'

STATIC_PATHS = [
  'images',
  'extra'
]
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
}
