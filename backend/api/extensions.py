from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_session import Session

db = SQLAlchemy()
server_session = Session()
bcrypt = Bcrypt()
migrate = Migrate(db=db)
