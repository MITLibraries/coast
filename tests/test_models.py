from __future__ import absolute_import

from coast import app, db
from coast.models import Author, DLC, Document


def test_empty_table(testapp):
    users = Author.query.all()
    assert users == []


def test_create_and_query_author(testapp):
    author = Author(name='Hermione Granger', mit_id=12345)
    db.session.add(author)
    db.session.commit()
    a = Author.query.first()
    assert "<Author name: 'Hermione Granger', MIT ID: '12345'>" == str(a)


def test_create_and_query_dlc(testapp):
    dlc = DLC(display_name='Ministry of Magic',
              canonical_name='MIT - Ministry of Magic')
    db.session.add(dlc)
    db.session.commit()
    d = DLC.query.first()
    assert "<DLC name: 'Ministry of Magic'>" == str(d)


def test_create_and_query_document(testapp):
    doc = Document(handle='hdl/98765',
                   title='A Treatise on the Expelliarmus Charm')
    db.session.add(doc)
    db.session.commit()
    d = Document.query.first()
    assert "<Document title: 'A Treatise on the Expelliarmus Charm'>" == str(d)
