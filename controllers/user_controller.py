"""User controller module"""

from services.user_service import UserService


class UserController:
    """User class to communicate directly with the services"""

    @staticmethod
    def get_by_id(user_id: int):
        """Get user resource"""
        return UserService.get_by_id(user_id)

    @staticmethod
    def get_all():
        """Get all user resources"""
        return UserService.get_all()

    @staticmethod
    def create():
        """Create user resource"""
        UserService.create()

    @staticmethod
    def delete_by_id(user_id: int):
        """Delete user resource"""
        return UserService.delete_by_id(user_id)

    @staticmethod
    def update_by_id(user_id: int):
        """Update user resource"""
        return UserService.update_by_id(user_id)
