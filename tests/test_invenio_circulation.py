# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 CERN.
#
# Invenio-Circulation is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from __future__ import absolute_import, print_function

from flask import Flask

from invenio_circulation import InvenioCirculation


def test_version():
    """Test version import."""
    from invenio_circulation import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioCirculation(app)
    assert 'invenio-circulation' in app.extensions

    app = Flask('testapp')
    ext = InvenioCirculation()
    assert 'invenio-circulation' not in app.extensions
    ext.init_app(app)
    assert 'invenio-circulation' in app.extensions


def test_view(app):
    """Test view."""
    InvenioCirculation(app)
    with app.test_client() as client:
        res = client.get("/")
        assert res.status_code == 200
        assert 'Welcome to Invenio-Circulation' in str(res.data)
