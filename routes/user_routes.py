from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user_service import create_user_service, loged, update_user_service, get_user_profile_service
from utils.helpers import response_success, response_error, validate_email
from models.user import User

user_bp = Blueprint('user', __name__)


@user_bp.route('/registrar', methods=['POST'])
def add_user():
    data = request.get_json()

    if not validate_email(data.get('email')):
        return response_error("Email Não é Válido", 400)

    response, status_code = create_user_service(**data)

    if status_code != 201:
        return response_error(response, status_code)

    return response_success("Usuário foi adicionado com sucesso.", response)


@user_bp.route('/entrar', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    access_token = loged(email, password)

    if access_token:
        return response_success("Login realizado", {"access_token": access_token})
    
    return response_error("Email ou Senha Incorretos", 400)


@user_bp.route('/perfil', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.get_user(user_id)
    if user:
        return response_success("Usuário Encontrado com sucesso", {"name": user['name']})
    else:
        return response_error("Usuário não encontrado", 404)


@user_bp.route('/alteraruser', methods=['PUT'])
@jwt_required()
def update_user():
    user_id = get_jwt_identity()
    data = request.get_json()
    response, status = update_user_service(user_id, data)
    if status != 200:
        return response_error(response, status)
    return response_success("Dados atualizados com sucesso.", response)


@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_user_profile():
    """
    Retorna todas as informações do usuário logado
    Requer: Header Authorization: Bearer <token>
    """
    user_id = get_jwt_identity()
    user, status_code = get_user_profile_service(user_id)
    
    if status_code != 200:
        return response_error(user, status_code)
    
    return response_success("Perfil do usuário recuperado com sucesso", user)
