"""Module to manage Product model"""

from database import db


class Product(db.Model):
    """Product table specification"""

    __tablename__ = "products"
    id = db.Column(db.Integet, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.String(256))
    author = db.Column(db.String(256))
    price = db.Column(db.FLOAT, nullable=False)
    image_path = db.Column(db.String(256))

    bookings = db.relationship("Booking")
    book_stores = db.relationship("BookStore")
