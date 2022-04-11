import os
import redis


class AppConfig:
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]

    # Server-sided session
    SESSION_TYPE = "redis"
    PERMANENT_SESSION_LIFETIME = 604800  # 1 week in seconds
    SESSION_REDIS = redis.from_url(os.environ["REDIS_URI"])
