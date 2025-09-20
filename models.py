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

# TODO: #5 Add relationship to User model