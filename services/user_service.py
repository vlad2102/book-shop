"""User service module"""
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from data_access_objects.user_dao import UserDao
from schemas.user_schema import UserSchema

# schema to manage single model data
userSchema = UserSchema()
# schema to manage multiple models data
userListSchema = UserSchema(many=True)


class UserService:
    """To support CRUD operations for user model"""

    @staticmethod
    def get_by_id(user_id: int):
        """Get user resource"""
        user_data = UserDao.fetch_by_id(user_id)
        return userSchema.dump(user_data)

    @staticmethod
    def get_all():
        """Get all user resources"""
        return userListSchema.dump(UserDao.fetch_all())

    @staticmethod
    def create():
        """Create user resource"""
        user_req_json = request.get_json()
        user = userSchema.load(user_req_json)
        UserDao.create(user)
        return userSchema.dump(user), 201

    @staticmethod
    def delete_by_id(user_id: int):
        """Delete user resource"""
        user = UserDao.fetch_by_id(user_id)
        UserDao.delete(user)
        return {'message': "User deleted successfully"}, 200

    @staticmethod
    def update_by_id(user_id: int):
        """Update user resource"""
        try:
            user_data = userSchema.dump(UserDao.fetch_by_id(user_id))
            user_data.update(request.get_json())
            user = userSchema.load(user_data)
            UserDao.update(user)
            return userSchema.dump(user), 200
        except ValidationError as error:
            return jsonify(details=str(error), status=400, title="Bad Request", type="about:blank")
        except IntegrityError as error:
            return jsonify(details=error.args[0], status=400, title="Bad Request", type="about:blank")
