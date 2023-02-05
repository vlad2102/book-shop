"""Module to manage Role model."""

from database import db


class Role(db.Model):
    """Role table specification."""

    __tablename__ = "roles"
    id = db.Column(db.Integet, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)

    users = db.relationship("User")
