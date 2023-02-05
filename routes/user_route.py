"""User routes module."""

from flask import request

from controllers.user_controller import UserController


def user_control():
    """URL to collect information about users or create new one."""
    match request.method:
        case 'POST':
            return UserController.create()
        case _:
            return UserController.get_all()


def user_manipulation(user_id: int):
    """URL to get, update or delete user information."""
    match request.method:
        case 'GET':
            return UserController.get_by_id(user_id)
        case 'PUT':
            return UserController.update_by_id(user_id)
        case 'DELETE':
            return UserController.delete_by_id(user_id)
