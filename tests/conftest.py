from __future__ import absolute_import

from config import APP_ROOT
import os
import pytest
import coast
from webtest import TestApp


@pytest.yield_fixture
def app():
    app = coast.app
    ctx = app.test_request_context()
    ctx.push()
    yield app
    ctx.pop()


@pytest.fixture
def db():
    db = coast.db.create_all()
    yield db
    coast.db.session.remove()
    coast.db.drop_all()


@pytest.fixture
def testapp(app, db):
    return TestApp(app)
