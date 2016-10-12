from coast import db

document_author = db.Table('document_author',
                           db.Column('id', db.Integer, primary_key=True),
                           db.Column('document_id', db.Integer,
                                     db.ForeignKey('document.id'),
                                     nullable=False),
                           db.Column('author_id', db.Integer,
                                     db.ForeignKey('author.id'),
                                     nullable=False))

document_dlc = db.Table('document_dlc',
                        db.Column('id', db.Integer, primary_key=True),
                        db.Column('document_id', db.Integer,
                                  db.ForeignKey('document.id'),
                                  nullable=False),
                        db.Column('dlc_id', db.Integer,
                                  db.ForeignKey('document.id'),
                                  nullable=False))


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), index=True)
    mit_id = db.Column(db.String(), index=True, unique=True)
    documents = db.relationship('Document', secondary=document_author,
                                backref=db.backref('authors'))

    def __repr__(self):
        return '<Author name: %r, MIT ID: %r>' % (self.name, self.mit_id)


class DLC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(), index=True)
    canonical_name = db.Column(db.String(), index=True)

    def __repr__(self):
        return '<DLC name: %r>' % (self.display_name)


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    handle = db.Column(db.String(), index=True, unique=True)
    title = db.Column(db.String(), index=True)

    def __repr__(self):
        return '<Document title: %r>' % (self.title)
