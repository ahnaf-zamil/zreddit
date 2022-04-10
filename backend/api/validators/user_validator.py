from werkzeug.exceptions import BadRequest

import re

EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def validate_username(username: str) -> str:
    if not username:
        raise BadRequest("Username not provided")

    if len(username) > 30 or len(username) < 3:
        raise BadRequest("Username length must be between 3 and 30 characters")

    return username


def validate_email(email: str) -> str:
    if not email:
        raise BadRequest("Email not provided")

    if len(email) > 255:
        raise BadRequest("Email length greater than 255")

    if not re.fullmatch(EMAIL_REGEX, email):
        raise BadRequest("Invalid Email")

    return email


def validate_password(password: str) -> str:
    if not password:
        raise BadRequest("Password not provided")

    if not len(password) >= 8:
        raise BadRequest("Password has to be at least 8 characters long")

    return password
