"""Product controller module"""

from services.product_service import ProductService


class ProductController:
    """Product class to communicate directly with the services"""

    @staticmethod
    def get_by_id(product_id: int):
        """Get product resource"""
        return ProductService.get_by_id(product_id)

    @staticmethod
    def get_all():
        """Get all product resources"""
        return ProductService.get_all()

    @staticmethod
    def create():
        """Create product resource"""
        ProductService.create()

    @staticmethod
    def delete_by_id(product_id: int):
        """Delete product resource"""
        return ProductService.delete_by_id(product_id)

    @staticmethod
    def update_by_id(product_id: int):
        """Update product resource"""
        return ProductService.update_by_id(product_id)
