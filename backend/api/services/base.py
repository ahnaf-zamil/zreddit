from api.extensions import db


class DatabaseAware:
    def __init__(self):
        self.db = db
