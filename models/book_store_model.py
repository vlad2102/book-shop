"""Module to manage BookStore model"""

from database import db


class BookStore(db.Model):
    """BookStore table specification"""

    __tablename__ = "book_store"
    id = db.Column(db.Integet, primary_key=True)
    product_id = db.Column(db.Integet, db.ForeignKey("products.id"))
    available = db.Column(db.Integet, default=0, nullable=False)
    booked = db.Column(db.Integet, default=0, nullable=False)
    sold = db.Column(db.Integet, default=0, nullable=False)
