from flask import Blueprint, request
from services.user_service import create_user_service, loged
from utils.helpers import response_success, response_error, validate_email


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
