import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from app.backend.config import Config
from app.backend.config import Config
from app.backend.database import Register, database
from app.backend.services.jobs_areas import Jobs
from app.backend.services.nations import JobCountry
from flask import Flask

def main():
    app = Flask(__name__)
    app.config.from_object(Config)

    database.init_app(app)

    with app.app_context():
        database.create_all()

    return app
