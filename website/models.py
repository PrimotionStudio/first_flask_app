from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String)
	email = db.Column(db.String, unique=True)
	password = db.Column(db.String)
	notes = db.relationship('Notes', backref='user', lazy='dynamic')

class Notes(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	note = db.Column(db.String(1000000))
	date = db.Column(db.DateTime, default=func.now())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))