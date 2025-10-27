from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.backend.security.auth import Auth

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
auth_service = Auth()

@auth_bp.route('/register', methods=['POST']) 
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not username or not email or not password:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400
    
    try:
        auth_service.register_user(username, email, password)
        return jsonify({"message": "Usuário registrado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400
    
    if auth_service.login_user(email, password):
        return jsonify({"message": "Login realizado com sucesso"}), 200
    
    return jsonify({"error": "Credenciais inválidas"}), 401

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    auth_service.logout_user()
    return jsonify({"message": "Logout realizado com sucesso"}), 200

@auth_bp.route('/generate-2fa', methods=['POST'])
@login_required
def generate_2fa():
    secret = auth_service.generate_2fa_secret()
    return jsonify({"secret": secret}), 200

@auth_bp.route('/verify-2fa', methods=['POST'])
@login_required
def verify_2fa():
    data = request.get_json()
    token = data.get('token')
    secret = data.get('secret') 
    
    if auth_service.verify_2fa(secret, token):
        return jsonify({"message": "2FA verificado com sucesso"}), 200
    
    return jsonify({"error": "Token inválido"}), 401

@auth_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }), 200
