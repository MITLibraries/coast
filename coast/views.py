from __future__ import absolute_import

from coast import app
from flask import flash, jsonify, redirect, render_template
from flask_bootstrap import Bootstrap
from .forms import AuthorForm
from .models import Author, Document

import json


@app.route('/', methods=['GET', 'POST'])
@app.route('/author', methods=['GET', 'POST'])
def author():
    form = AuthorForm()
    if form.validate_on_submit():
        if form.name.data:
            aname = form.name.data
            authors = Author.query.filter(Author.name.contains(aname)).all()
            if authors:
                results = format_authors(authors)
                return render_template('author.html', form=form,
                                       authors=results)
            else:
                flash('Author "%s" not found' % aname, 'warning')
                return render_template('author.html', form=form)
        elif form.mit_id.data:
            author = Author.query.filter_by(mit_id=form.mit_id.data).all()
            if author:
                results = format_authors(author)
                return render_template('author.html', form=form,
                                       authors=results)
            else:
                flash('Author %s not found' % (form.mit_id.data), 'warning')
                return render_template('author.html', form=form)
        else:
            authors = Author.query.all()
            results = format_authors(authors)
            return render_template('author.html', form=form, authors=results)
    return render_template('author.html', form=form)


def format_authors(authors):
    results = []
    for author in authors:
        results.append({'name': author.name,
                        'mit_id': author.mit_id})
    return results
