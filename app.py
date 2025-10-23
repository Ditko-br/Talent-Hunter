from config import Config
from models.register import database
from flask import Flask

def main():
    app = Flask(__name__)
    app.config.from_object(Config)

    database.init_app(app)

    with app.app_context():
        database.create_all()

    return app