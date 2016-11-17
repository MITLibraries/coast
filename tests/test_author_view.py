from __future__ import absolute_import

from coast import app, db
from coast.models import Author
from collections import OrderedDict


def test_index_page_loads(testapp):
    response = testapp.get('/')
    assert response.status_code == 200

    response = testapp.get('/author')
    assert response.status_code == 200


def test_empty_table(testapp):
    users = Author.query.all()
    assert users == []


def test_query_author_by_name(testapp):
    response = testapp.post('/author',
                            params=OrderedDict([('name', 'hermione granger')]))
    assert 'Author &#34;hermione granger&#34; not found' in response

    author = Author(name='Hermione Granger', mit_id=12345)
    db.session.add(author)
    db.session.commit()

    response = testapp.post('/author',
                            params=OrderedDict([('name', 'hermione granger')]))
    assert '<td>Hermione Granger</td>' in response


def test_query_author_by_mit_id(testapp):
    response = testapp.post('/author',
                            params=OrderedDict([('mit_id', '12345')]))
    assert 'Author 12345 not found' in response

    author = Author(name='Hermione Granger', mit_id=12345)
    db.session.add(author)
    db.session.commit()

    response = testapp.post('/author',
                            params=OrderedDict([('mit_id', '12345')]))
    assert '<td>Hermione Granger</td>' in response


def test_query_all_authors(testapp):
    response = testapp.post('/author',
                            params=OrderedDict([('name', ''), ('mit_id', '')]))
    assert 'div class="alert alert-warning' not in response
    assert '<table class="table table-condensed">' not in response

    db.session.add(Author(name='Hermione Granger', mit_id=12345))
    db.session.add(Author(name='Harry Potter', mit_id=67890))
    db.session.commit()

    response = testapp.post('/author',
                            params=OrderedDict([('name', ''), ('mit_id', '')]))
    assert '<td>Hermione Granger</td>' in response
    assert '<td>Harry Potter</td>' in response
