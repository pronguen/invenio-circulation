# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Invenio module for the circulation of bibliographic items."""

from __future__ import absolute_import, print_function

from .ext import InvenioCirculation
from .version import __version__

__all__ = ('__version__', 'InvenioCirculation')
