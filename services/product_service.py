"""Product service module"""
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from data_access_objects.product_dao import ProductDao
from schemas.product_schema import ProductSchema

# schema to manage single model data
productSchema = ProductSchema()
# schema to manage multiple models data
productListSchema = ProductSchema(many=True)


class ProductService:
    """To support CRUD operations for product model"""

    @staticmethod
    def get_by_id(product_id: int):
        """Get product resource"""
        product_data = ProductDao.fetch_by_id(product_id)
        return productSchema.dump(product_data)

    @staticmethod
    def get_all():
        """Get all product resources"""
        return productListSchema.dump(ProductDao.fetch_all())

    @staticmethod
    def create():
        """Create product resource"""
        product_req_json = request.get_json()
        product = productSchema.load(product_req_json)
        ProductDao.create(product)
        return productSchema.dump(product), 201

    @staticmethod
    def delete_by_id(product_id: int):
        """Delete product resource"""
        product = ProductDao.fetch_by_id(product_id)
        ProductDao.delete(product)
        return {'message': "Product deleted successfully"}, 200

    @staticmethod
    def update_by_id(product_id: int):
        """Update product resource"""
        try:
            product_data = productSchema.dump(ProductDao.fetch_by_id(product_id))
            product_data.update(request.get_json())
            product = productSchema.load(product_data)
            ProductDao.update(product)
            return productSchema.dump(product), 200
        except ValidationError as error:
            return jsonify(details=str(error), status=400, title="Bad Request", type="about:blank")
        except IntegrityError as error:
            return jsonify(details=error.args[0], status=400, title="Bad Request", type="about:blank")
