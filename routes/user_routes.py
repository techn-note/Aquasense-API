from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user_service import create_user_service, loged
from utils.helpers import response_success, response_error, validate_email
from models.user import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['POST'])
def add_user():
    data = request.get_json()

    if not validate_email(data.get('email')):
        return response_error("Email is not valid.", 400)

    response, status_code = create_user_service(**data)

    if status_code != 201:
        return response_error(response, status_code)

    return response_success("Usuário foi adicionado com sucesso.", response)


@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    access_token = loged(email, password)

    if access_token:
        return response_success("Login successful", {"access_token": access_token})
    
    return response_error("Bad credentials", 400)


@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.get_user(user_id)
    if user:
        return response_success("User profile fetched successfully.", {"name": user['name']})
    else:
        return response_error("User not found.", 404)