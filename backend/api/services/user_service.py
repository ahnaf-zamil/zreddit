from typing import Optional
from werkzeug.exceptions import Conflict, Unauthorized
from api.models.user import User
from .base import DatabaseAware
from api.extensions import bcrypt


class UserService(DatabaseAware):
    def create_user(self, username: str, email: str, password: str) -> User:
        hashed_password = bcrypt.generate_password_hash(password)

        existing_user = (
            User.query.filter(
                (User.email == email) | (User.username == username)
            ).first()
            is not None
        )

        if existing_user:
            raise Conflict("A user with same email or username already exists")

        new_user = User(username=username, email=email, password=hashed_password)

        self.db.session.add(new_user)
        self.db.session.commit()

        return new_user

    def authenticate_user(self, email: str, password: str):
        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
            raise Unauthorized("Invalid credentials")

        if not bcrypt.check_password_hash(existing_user.password, password):
            raise Unauthorized("Invalid credentials")

        return existing_user.id

    def get_user(self, user_id: str) -> Optional[User]:
        user = User.query.filter_by(id=user_id).first()
        return user
