"""Booking service module"""
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from data_access_objects.booking_dao import BookingDao
from models.booking_schema import BookingSchema

# schema to manage single model data
bookingSchema = BookingSchema()
# schema to manage multiple models data
bookingListSchema = BookingSchema(many=True)


class BookingService:
    """To support CRUD operations for booking model"""

    @staticmethod
    def get_by_id(booking_id: int):
        """Get booking resource"""
        booking_data = BookingDao.fetch_by_id(booking_id)
        return bookingSchema.dump(booking_data)

    @staticmethod
    def get_all():
        """Get all booking resources"""
        return bookingListSchema.dump(BookingDao.fetch_all())

    @staticmethod
    def create():
        """Create booking resource"""
        booking_req_json = request.get_json()
        booking = bookingSchema.load(booking_req_json)
        BookingDao.create(booking)
        return bookingSchema.dump(booking), 201

    @staticmethod
    def delete_by_id(booking_id: int):
        """Delete booking resource"""
        booking = BookingDao.fetch_by_id(booking_id)
        BookingDao.delete(booking)
        return {'message': "Booking deleted successfully"}, 200

    @staticmethod
    def update_by_id(booking_id: int):
        """Update booking resource"""
        try:
            booking_data = bookingSchema.dump(BookingDao.fetch_by_id(booking_id))
            booking_data.update(request.get_json())
            booking = bookingSchema.load(booking_data)
            BookingDao.update(booking)
            return bookingSchema.dump(booking), 200
        except ValidationError as error:
            return jsonify(details=str(error), status=400, title="Bad Request", type="about:blank")
        except IntegrityError as error:
            return jsonify(details=error.args[0], status=400, title="Bad Request", type="about:blank")
