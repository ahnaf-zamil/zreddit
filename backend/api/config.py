import os


class AppConfig:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
