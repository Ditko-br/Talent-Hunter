from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from app.backend.database.register import database, RegisterUser

users_bp = Blueprint('users', __name__, url_prefix='/api/users')

@users_bp.route('/profile', methods=['GET'])
@login_required
def get_profile():
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }), 200

@users_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile():
    data = request.get_json()
    username = data.get('username')
    
    if username:
        current_user.username = username
        database.session.commit()
        return jsonify({"message": "Perfil atualizado"}), 200
    
    return jsonify({"error": "Dados inválidos"}), 400