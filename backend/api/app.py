from flask import Flask
from api.extensions import db, migrate, bcrypt, server_session
from api.config import AppConfig


def make_app():
    app = Flask(__name__)
    app.config.from_object(AppConfig)

    db.init_app(app)
    bcrypt.init_app(app)
    server_session.init_app(app)
    migrate.init_app(app)

    from api.routers.user_routes import user_router

    app.register_blueprint(user_router)

    return app
