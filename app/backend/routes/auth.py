from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.backend.security.auth import Auth

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
auth_service = Auth()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    enable_2fa = data.get('enable_2fa', False)

    if not username or not email or not password:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    try:
        user = auth_service.register_user(username, email, password, enable_2fa=enable_2fa)
        return jsonify({"message": "Usuário registrado", "id": user.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    res = auth_service.login_user(email, password)
    if res.get("ok"):
        return jsonify({"message": "Login realizado"}), 200
    if res.get("2fa_required"):
        return jsonify({"message": "2FA required", "email": res.get("email")}), 202
    return jsonify({"error": res.get("error", "Credenciais inválidas")}), 401

@auth_bp.route('/verify-2fa', methods=['POST'])
def verify_2fa():
    data = request.get_json() or {}
    email = data.get('email')
    token = data.get('token')
    if not email or not token:
        return jsonify({"error": "Email e token são obrigatórios"}), 400

    res = auth_service.verify_2fa_and_login(email, token)
    if res.get("ok"):
        return jsonify({"message": "2FA verificado e login finalizado"}), 200
    return jsonify({"error": res.get("error", "Token inválido")}), 401

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    auth_service.logout_user()
    return jsonify({"message": "Logout realizado"}), 200

@auth_bp.route('/generate-2fa', methods=['POST'])
@login_required
def generate_2fa():
    # gera secret e grava no usuário atual
    secret = auth_service.generate_2fa_secret(current_user.email)
    # no frontend: converta secret para QR code (otpauth://) ou mostre a string
    return jsonify({"secret": secret}), 200

@auth_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }), 200