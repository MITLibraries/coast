from __future__ import absolute_import

from coast.models import Author


def test_index_page_loads(testapp):
    response = testapp.get('/')
    assert response.status_code == 200


def test_empty_table(testapp):
    users = Author.query.all()
    assert users == []
