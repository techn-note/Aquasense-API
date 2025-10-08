from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.peixe_service import (
    create_peixe_service,
    get_peixe_service_name,
    get_peixe_service,
    get_all_peixes_service,
    update_peixe_service,
    delete_peixe_service
)
from utils.helpers import response_success, response_error

peixe_bp = Blueprint('peixe', __name__)

@peixe_bp.route('/peixes', methods=['POST'])
@jwt_required()
def add_peixe():
    user_id = get_jwt_identity()
    data = request.get_json()
    data["user_id"] = user_id  # adiciona user_id ao data
    response, status_code = create_peixe_service(**data)
    
    if status_code != 201:
        return response_error(response, status_code)
    
    return response_success("Peixe foi adicionado com sucesso.", response)

@peixe_bp.route('/peixes/<string:peixe_id>', methods=['GET'])
@jwt_required()
def get_peixe(peixe_id):
    user_id = get_jwt_identity()
    response, status_code = get_peixe_service(peixe_id, user_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Peixe encontrado.", response)

@peixe_bp.route('/peixes', methods=['GET'])
@jwt_required()
def get_all_peixes():
    user_id = get_jwt_identity()
    response = get_all_peixes_service(user_id)
    return response_success("Lista de peixes retornada com sucesso.", response)

@peixe_bp.route('/peixes/nome/<string:name>', methods=['GET'])
@jwt_required()
def get_peixe_by_name(name):
    user_id = get_jwt_identity()
    response, status_code = get_peixe_service_name(name, user_id)

    if status_code != 200:
        return response_error(response, status_code)

    peixe = response.get("data")
    if peixe:
        peixe["_id"] = str(peixe["_id"])

    return response_success("Peixe encontrado.", response)

@peixe_bp.route('/peixes/<string:peixe_id>', methods=['PUT'])
@jwt_required()
def update_peixe(peixe_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    response, status_code = update_peixe_service(peixe_id, data, user_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Peixe atualizado com sucesso.", response)

@peixe_bp.route('/peixes/<string:peixe_id>', methods=['DELETE'])
@jwt_required()
def delete_peixe(peixe_id):
    user_id = get_jwt_identity()
    response, status_code = delete_peixe_service(peixe_id, user_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Peixe deletado com sucesso.", response)
