from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime, timezone
from app import db

# TODO: #4 Define User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    standups = db.relationship('Standup', backref='user', lazy=True)
    journals = db.relationship('Journal', backref='user', lazy=True)

class Standup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.now(timezone.utc).date())
    yesterday = db.Column(db.Text, nullable=False)
    today = db.Column(db.Text, nullable=False)
    blockers = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    public = db.Column(db.Boolean, default=False, nullable=False)

# TODO: #5 Add Standup-User relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    __table_args__ = (db.UniqueConstraint('date', 'user_id', name='uix_user_date'))

class Journal(db.Model):
    id = db.Column(db.Integet, primary_key=True)
    title= db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    public = db.Column(db.Boolean, default=False, nullable=False)

# TODO: Add Journal-User relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)