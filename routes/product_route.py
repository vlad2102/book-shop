"""Product routes module"""

from flask import request

from controllers.product_controller import ProductController


def product_control():
    """URL to collect information about products or create new one"""
    match request.method:
        case 'POST':
            return ProductController.create()
        case _:
            return ProductController.get_all()


def product_manipulation(product_id: int):
    """URL to get, update or delete product information"""
    match request.method:
        case 'GET':
            return ProductController.get_by_id(product_id)
        case 'PUT':
            return ProductController.update_by_id(product_id)
        case 'DELETE':
            return ProductController.delete_by_id(product_id)
