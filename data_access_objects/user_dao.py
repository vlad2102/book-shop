"""Module for User Data Access Object."""
from typing import Final

from database import db
from models.user_model import User


class UserDao:
    """Data Access Object for User Model."""

    _USER_NOT_FOUND_PATTERN: Final = "User not found for id: {user_id}"

    @staticmethod
    def create(user: User) -> None:
        """Create user in database"""
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def fetch_by_id(user_id: int) -> User:
        """Gets user by id from database"""
        return db.session.query(User).get_or_404(
            user_id, description=UserDao._USER_NOT_FOUND_PATTERN.format(user_id=user_id)
        )

    @staticmethod
    def fetch_all() -> list[User]:
        """Returns all users from database"""
        return db.session.query(User).all()

    @staticmethod
    def delete_by_id(user_id: int) -> None:
        """Deletes user from database"""
        user = db.session.query(User).filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def update(user: User) -> None:
        """Updates user in database"""
        db.session.merge(user)
        db.session.commit()
