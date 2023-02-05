"""Module to manage User model."""

from database import db


class User(db.Model):
    """User table specification."""

    __tablename__ = "users"
    id = db.Column(db.Integet, primary_key=True)
    name = db.Column(db.String(256))
    address = db.Column(db.String(256))
    email = db.Column(db.String(256))
    role_id = db.Column(db.Integet, db.ForeignKey("roles.id"))
    login = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    bookings = db.relationship("Booking")
