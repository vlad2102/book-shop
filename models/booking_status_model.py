"""Module to manage BookingStatus model."""

from database import db


class BookingStatus(db.Model):
    """BookingStatus table specification."""

    __tablename__ = "booking_status"
    id = db.Column(db.Integet, primary_key=True)
    name = db.Column(db.String(256), unique=True, nullable=False)

    bookings = db.relationship("Booking")
