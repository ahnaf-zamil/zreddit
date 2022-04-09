from flask import Blueprint
from api.services import user_service

user_router = Blueprint("user", __name__, url_prefix="/users")


@user_router.get("/@me")
def get_current_user():
    return user_service.create_user()
