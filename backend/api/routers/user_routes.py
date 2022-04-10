from flask import Blueprint, request
from api.services import user_service
from api.validators.user_validator import (
    validate_email,
    validate_password,
    validate_username,
)

user_router = Blueprint("user", __name__, url_prefix="/users")


@user_router.get("/@me")
def get_current_user():
    return user_service.create_user()


@user_router.post("/register")
def register_user():
    username = validate_username(request.json.get("username"))
    email = validate_email(request.json.get("email"))
    password = validate_password(request.json.get("password"))

    result = user_service.create_user(username, email, password)

    return {"success": result}


@user_router.post("/login")
def login_user():
    email = validate_email(request.json.get("email"))
    password = validate_password(request.json.get("password"))

    user_id = user_service.authenticate_user(email, password)

    # User_id will be used to store server sided session

    return {"success": True}
