import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from flask_login import LoginManager
from app.backend.config.config import Config
from app.backend.database.register import database, RegisterUser
from app.backend.schemas.schemas import ma
from app.backend.routes.auth import auth_bp
from app.backend.routes.search import search_bp
from app.backend.routes.companies import companies_bp
from app.backend.routes.users import users_bp
from app.backend.services.email import mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # init extensions
    database.init_app(app)
    ma.init_app(app)
    mail.init_app(app)

    # login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return RegisterUser.query.get(int(user_id))

    # register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(companies_bp)
    app.register_blueprint(users_bp)

    with app.app_context():
        database.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)