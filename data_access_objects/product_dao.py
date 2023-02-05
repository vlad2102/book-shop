"""Module for Product Data Access Object."""
from typing import Final

from database import db
from models.product_model import Product


class ProductDao:
    """Data Access Object for Product Model."""

    _PRODUCT_NOT_FOUND_PATTERN: Final = "Product not found for id: {product_id}"

    @staticmethod
    def create(product: Product) -> None:
        """Create product in database"""
        db.session.add(product)
        db.session.commit()

    @staticmethod
    def fetch_by_id(product_id: int) -> Product:
        """Gets product by id from database"""
        return db.session.query(Product).get_or_404(
            product_id, description=ProductDao._PRODUCT_NOT_FOUND_PATTERN.format(product_id=product_id)
        )

    @staticmethod
    def fetch_all() -> list[Product]:
        """Returns all products from database"""
        return db.session.query(Product).all()

    @staticmethod
    def delete_by_id(product_id: int) -> None:
        """Deletes product from database"""
        product = db.session.query(Product).filter_by(id=product_id).first()
        db.session.delete(product)
        db.session.commit()

    @staticmethod
    def update(product: Product) -> None:
        """Updates product in database"""
        db.session.merge(product)
        db.session.commit()
