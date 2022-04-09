from api.extensions import db


class BaseService:
    def __init__(self):
        self.db = db
