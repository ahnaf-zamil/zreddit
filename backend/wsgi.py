from dotenv import load_dotenv

load_dotenv()

from api.app import make_app, migrate
from api.models import *

app = make_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
