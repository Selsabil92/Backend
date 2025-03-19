 # Gestion des utilisateurs et authentification JWT
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User

auth = Blueprint('auth', __name__)

@auth.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.authenticate(username, password)
    if not user:
        return jsonify({"error": "Identifiants invalides"}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)
