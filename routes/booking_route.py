"""Booking routes module"""

from flask import request

from controllers.booking_controller import BookingController


def booking_control():
    """URL to collect information about bookings or create new one"""
    match request.method:
        case 'POST':
            return BookingController.create()
        case _:
            return BookingController.get_all()


def booking_manipulation(booking_id: int):
    """URL to get, update or delete booking information"""
    match request.method:
        case 'GET':
            return BookingController.get_by_id(booking_id)
        case 'PUT':
            return BookingController.update_by_id(booking_id)
        case 'DELETE':
            return BookingController.delete_by_id(booking_id)
