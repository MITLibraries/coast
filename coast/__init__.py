from __future__ import absolute_import

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import configure_app

app = Flask(__name__)
configure_app(app)
db = SQLAlchemy(app)

from coast import views, models
