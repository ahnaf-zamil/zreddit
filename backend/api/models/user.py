from api.extensions import db
from uuid import uuid4


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(32), primary_key=True, default=lambda: uuid4().hex)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.LargeBinary(60), nullable=False)

    def to_json(self, show_email=False):
        payload = {"id": self.id, "username": self.username}

        if show_email:
            payload["email"] = self.email

        return payload
