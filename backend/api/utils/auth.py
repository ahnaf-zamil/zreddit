from functools import wraps
from flask import session
from api.services import user_service
from werkzeug.exceptions import Unauthorized


def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        user_id = session.get("user_id")
        if not user_id:
            raise Unauthorized("Not logged in")

        user = user_service.get_user(user_id)

        if not user:
            raise Unauthorized("Not logged in")

        return f(user, *args, **kwargs)

    return inner
