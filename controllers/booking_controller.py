"""Booking controller module"""

from services.booking_service import BookingService


class BookingController:
    """Booking class to communicate directly with the services"""

    @staticmethod
    def get_by_id(booking_id: int):
        """Get booking resource"""
        return BookingService.get_by_id(booking_id)

    @staticmethod
    def get_all():
        """Get all booking resources"""
        return BookingService.get_all()

    @staticmethod
    def create():
        """Create booking resource"""
        BookingService.create()

    @staticmethod
    def delete_by_id(booking_id: int):
        """Delete booking resource"""
        return BookingService.delete_by_id(booking_id)

    @staticmethod
    def update_by_id(booking_id: int):
        """Update booking resource"""
        return BookingService.update_by_id(booking_id)
