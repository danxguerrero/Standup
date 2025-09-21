from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from app import db

# TODO: #4 Define User model


class Standup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.now(timezone.utc).date())
    yesterday = db.Column(db.Text, nullable=False)
    today = db.Column(db.Text, nullable=False)
    blockers = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    public = db.Column(db.Boolean, default=False, nullable=False)

# TODO: #5 Add Standup-User relationship

class Journal(db.Model):
    id = db.Column(db.Integet, primary_key=True)
    title= db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    public = db.Column(db.Boolean, default=False, nullable=False)

# TODO: Add Journal-User relationship