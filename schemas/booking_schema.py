"""Booking ORM Schema."""

from database import db
from dependencies import ma
from models.booking_model import Booking


class BookingSchema(ma.SQLAlchemySchema):
    """Booking schema."""

    class Meta:
        model = Booking
        load_instance = True
        sqla_session = db.session

    id = ma.auto_field()
    user_id = ma.auto_field()
    product_id = ma.auto_field()
    delivery_address = ma.auto_field()
    delivery_date = ma.auto_field()
    delivery_time = ma.auto_field()
    status_id = ma.auto_field()
