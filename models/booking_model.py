"""Module to manage Booking model"""

from database import db


class Booking(db.Model):
    """Booking table specification"""

    __tablename__ = "bookings"
    id = db.Column(db.Integet, primary_key=True)
    user_id = db.Column(db.Integet, db.ForeignKey("users.id"))
    product_id = db.Column(db.Integet, db.ForeignKey("products.id"))
    delivery_address = db.Column(db.String(256), nullable=False)
    delivery_date = db.Column(db.Date, nullable=False)
    delivery_time = db.Column(db.DateTime, nullable=False)
    status_id = db.Column(db.Integet, db.ForeignKey("booking_status.id"))
