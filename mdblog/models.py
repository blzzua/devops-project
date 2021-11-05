from enum import unique
from flask_sqlalchemy import SQLAlchemy

from mdblog.default import PASSWORD

db = SQLAlchemy()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    PASSWORD = db.Column(db.String)