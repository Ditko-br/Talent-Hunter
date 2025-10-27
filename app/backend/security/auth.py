from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.backend.database import database, RegisterUser
import pyotp

class Auth:
    def __init__(self):
        pass

    def register_user(self, username, email, password):
        hashed_password = generate_password_hash(password, method='sha256')
        user = RegisterUser(username=username, email=email, hashed_password=hashed_password)
        database.session.add(user)
        database.session.commit()

    def login_user(self, email, password):
        user = RegisterUser.query.filter_by(email=email).first()
        if user and check_password_hash(user.hashed_password, password):
            login_user(user)
            return True
        return False

    def logout_user(self):
        logout_user()
        return True

    def generate_2fa_secret(self):
        return pyotp.random_base32()

    def verify_2fa(self, secret, token):
        totp = pyotp.TOTP(secret)
        return totp.verify(token)
    