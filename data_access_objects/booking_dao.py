"""Module for Booking Data Access Object."""
from typing import Final

from database import db
from models.booking_model import Booking


class BookingDao:
    """Data Access Object for Booking Model."""

    _BOOKING_NOT_FOUND_PATTERN: Final = "Booking not found for id: {booking_id}"

    @staticmethod
    def create(booking: Booking) -> None:
        """Create booking in database"""
        db.session.add(booking)
        db.session.commit()

    @staticmethod
    def fetch_by_id(booking_id: int) -> Booking:
        """Gets booking by id from database"""
        return db.session.query(Booking).get_or_404(
            booking_id, description=BookingDao._BOOKING_NOT_FOUND_PATTERN.format(booking_id=booking_id)
        )

    @staticmethod
    def fetch_all() -> list[Booking]:
        """Returns all bookings from database"""
        return db.session.query(Booking).all()

    @staticmethod
    def delete_by_id(booking_id: int) -> None:
        """Deletes booking from database"""
        booking = db.session.query(Booking).filter_by(id=booking_id).first()
        db.session.delete(booking)
        db.session.commit()

    @staticmethod
    def update(booking: Booking) -> None:
        """Updates booking in database"""
        db.session.merge(booking)
        db.session.commit()
