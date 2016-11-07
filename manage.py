#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from config import configure_app
from coast import app, db

from coast import views, models

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())


if __name__ == '__main__':
    manager.run()
