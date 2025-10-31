from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

database = SQLAlchemy()

class RegisterUser(database.Model, UserMixin):
    __tablename__ = "users_registers"

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(50), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    hashed_password = database.Column(database.String(128), nullable=False)
    # secret para 2FA (TOTP). Guarde aqui o base32 (nullable até o usuário habilitar)
    twofa_secret = database.Column(database.String(64), nullable=True)

    def __repr__(self):
        return f"<User {self.username}>"

