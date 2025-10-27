import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask
from flask_login import LoginManager
from app.backend.config.config import Config
from app.backend.database.register import database, RegisterUser
from app.backend.routes.auth import auth_bp
from app.backend.routes.search import search_bp
from app.backend.routes.companies import companies_bp

def main():
    app = Flask(__name__)
    app.config.from_object(Config)
    database.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        return RegisterUser.query.get(int(user_id))

    app.register_blueprint(auth_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(companies_bp)

    with app.app_context():
        database.create_all()

    return app

if __name__ == '__main__':
    app = main()
    app.run(debug=True)