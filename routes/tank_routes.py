from flask import Blueprint, request
from services.tank_service import create_tank_service, get_tank_service, get_all_tanks_service, update_tank_service, delete_tank_service
from utils.helpers import response_success, response_error

tank_bp = Blueprint('tank', __name__)

@tank_bp.route('/tanks', methods=['POST'])
def add_tank():
    data = request.get_json()
    response, status_code = create_tank_service(**data)

    if status_code != 201:
        return response_error(response, status_code)

    return response_success("Tanque foi adicionado com sucesso.", response)

@tank_bp.route('/tanks/<string:tank_id>', methods=['GET'])
def get_tank(tank_id):
    response, status_code = get_tank_service(tank_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Tanque encontrado.", response)

@tank_bp.route('/tanks', methods=['GET'])
def get_all_tanks():
    response, status_code = get_all_tanks_service()

    return response_success("Tanques encontrados.", response)

@tank_bp.route('/tanks/<string:tank_id>', methods=['PUT'])
def update_tank(tank_id):
    data = request.get_json()
    response, status_code = update_tank_service(tank_id, data)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Tanque atualizado com sucesso.", response)

@tank_bp.route('/tanks/<string:tank_id>', methods=['DELETE'])
def delete_tank(tank_id):
    response, status_code = delete_tank_service(tank_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Tanque excluído com sucesso.", response)
