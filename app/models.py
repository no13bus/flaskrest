from app import db
from flask.ext.login import UserMixin
from datetime import datetime
import uuid

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    birth_date = db.Column(db.Date)

    def to_dict(self):
        pass

class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    vendor = db.Column(db.Unicode)
    purchase_time = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    owner = db.relationship('Person', backref=db.backref('computers',lazy='dynamic'))

    def to_dict(self):
        pass

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode)
    content = db.Column(db.Unicode)
    
    def to_dict(self):
        res = dict()
        for c in self.__table__.columns:
            value = getattr(self, c.name)
            if isinstance(value, datetime):
                res[c.name] = value.isoformat()
            elif isinstance(value, uuid.UUID):
                res[c.name] = str(value)
            else:
                res[c.name] = value
        return res

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode)
    password = db.Column(db.Unicode)

    def to_dict(self):
        res = dict()
        for c in self.__table__.columns:
            value = getattr(self, c.name)
            if isinstance(value, datetime):
                res[c.name] = value.isoformat()
            elif isinstance(value, uuid.UUID):
                res[c.name] = str(value)
            else:
                res[c.name] = value
        return res


# /usr/local/lib/python2.7/dist-packages/sqlalchemy/engine/default.py:573: SAWarning: Unicode type received non-unicodebind param value.