from flask_login import login_user as flask_login_user, logout_user as flask_logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.backend.database.register import database, RegisterUser
import pyotp

class Auth:
    def __init__(self):
        pass

    def register_user(self, username: str, email: str, password: str, enable_2fa: bool = False):
        hashed_password = generate_password_hash(password, method='sha256')
        user = RegisterUser(username=username, email=email, hashed_password=hashed_password)
        if enable_2fa:
            user.twofa_secret = pyotp.random_base32()
        database.session.add(user)
        database.session.commit()
        return user

    def login_user(self, email: str, password: str):
        """
        Verifica credenciais. Se usuário tem 2FA configurado, não finaliza o login:
        retorna {'2fa_required': True} para o frontend solicitar o token.
        Se não há 2FA, faz login e retorna {'ok': True}.
        """
        user = RegisterUser.query.filter_by(email=email).first()
        if not user:
            return {"ok": False, "error": "Usuário não encontrado"}
        if not check_password_hash(user.hashed_password, password):
            return {"ok": False, "error": "Senha inválida"}

        if user.twofa_secret:
            # senha ok, mas 2FA habilitado -> exigir token
            return {"ok": False, "2fa_required": True, "email": user.email}
        # senha ok, sem 2FA -> finalizar sessão
        flask_login_user(user)
        return {"ok": True}

    def verify_2fa_and_login(self, email: str, token: str):
        """
        Verifica token TOTP e, se válido, realiza login.
        """
        user = RegisterUser.query.filter_by(email=email).first()
        if not user or not user.twofa_secret:
            return {"ok": False, "error": "Usuário não encontrado ou 2FA não configurado"}

        totp = pyotp.TOTP(user.twofa_secret)
        if totp.verify(token):
            flask_login_user(user)
            return {"ok": True}
        return {"ok": False, "error": "Token inválido"}

    def generate_2fa_secret(self, email: str = None):
        """
        Gera um secret para o usuário. Se email for informado, salva no usuário.
        Retorna o secret (base32) para ser mostrado via QR ou string.
        """
        secret = pyotp.random_base32()
        if email:
            user = RegisterUser.query.filter_by(email=email).first()
            if user:
                user.twofa_secret = secret
                database.session.commit()
        return secret

    def logout_user(self):
        flask_logout_user()
        return True