from flask import Blueprint, request
from services.tank_service import (
    create_tank_service,
    get_tank_service_name,
    get_tank_service,
    get_all_tanks_service,
    update_tank_service,
    delete_tank_service
)
from utils.helpers import response_success, response_error
from flask_jwt_extended import jwt_required, get_jwt_identity

tank_bp = Blueprint('tank', __name__)

@tank_bp.route('/tanque', methods=['POST'])
@jwt_required()
def add_tank():
    data = request.get_json()
    data["user_id"] = get_jwt_identity()

    response, status_code = create_tank_service(**data)
    if status_code != 201:
        return response_error(response, status_code)

    return response_success("Tanque foi adicionado com sucesso.", response)


@tank_bp.route('/tanque/<string:tank_id>', methods=['GET'])
@jwt_required()
def get_tank(tank_id):
    user_id = get_jwt_identity()
    response, status_code = get_tank_service(tank_id, user_id)
    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Tanque encontrado.", response)


@tank_bp.route('/tanque/nome/<string:name>', methods=['GET'])
@jwt_required()
def get_tank_by_name(name):
    user_id = get_jwt_identity()
    response, status_code = get_tank_service_name(name, user_id)
    if status_code != 200:
        return response_error(response, status_code)

    tank = response.get("data")
    if tank:
        tank["_id"] = str(tank["_id"])

    return response_success("Tanque encontrado.", response)


@tank_bp.route('/tanque', methods=['GET'])
@jwt_required()
def get_all_tanks():
    user_id = get_jwt_identity()
    response, status_code = get_all_tanks_service(user_id)
    return response_success("Tanques encontrados.", response)


@tank_bp.route('/tanque/<string:tank_id>', methods=['PUT'])
@jwt_required()
def update_tank(tank_id):
    data = request.get_json()
    user_id = get_jwt_identity()
    response, status_code = update_tank_service(tank_id, data, user_id)
    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Tanque atualizado com sucesso.", response)


@tank_bp.route('/tanque/<string:tank_id>', methods=['DELETE'])
@jwt_required()
def delete_tank(tank_id):
    user_id = get_jwt_identity()
    response, status_code = delete_tank_service(tank_id, user_id)
    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Tanque excluído com sucesso.", response)
