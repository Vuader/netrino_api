# -*- coding: utf-8 -*-
"""Netrino API"""

from tachyonic.netrino_api import metadata
from . import views, middleware


__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright
