from flask import Blueprint, request, g
from services.sensores_service import (
    create_sensor_service,
    get_sensor_service,
    get_all_sensores_service,
    update_sensor_service,
    delete_sensor_service,
    get_latest_sensor_data_service,
    get_last_10_sensor_data_service
)
from utils.helpers import response_success, response_error
from flask_jwt_extended import jwt_required, get_jwt_identity

sensores_bp = Blueprint('sensores', __name__)


@sensores_bp.route('/sensores', methods=['POST'])
@jwt_required()
def add_sensor():
    data = request.get_json()
    data['user_id'] = get_jwt_identity()
    response, status_code = create_sensor_service(**data)

    if status_code != 201:
        return response_error(response, status_code)

    return response_success("Sensor foi adicionado com sucesso.", {"id": response})


@sensores_bp.route('/sensores/<string:sensor_id>', methods=['GET'])
@jwt_required()
def get_sensor(sensor_id):
    user_id = get_jwt_identity()
    response, status_code = get_sensor_service(sensor_id, user_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Sensor encontrado.", response)


@sensores_bp.route('/sensores', methods=['GET'])
@jwt_required()
def get_all_sensores():
    user_id = get_jwt_identity()
    response, status_code = get_all_sensores_service(user_id)
    return response_success("Sensores encontrados.", response)


@sensores_bp.route('/sensores/<string:sensor_id>', methods=['PUT'])
@jwt_required()
def update_sensor(sensor_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    response, status_code = update_sensor_service(sensor_id, data, user_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Sensor atualizado com sucesso.", response)


@sensores_bp.route('/sensores/<string:sensor_id>', methods=['DELETE'])
@jwt_required()
def delete_sensor(sensor_id):
    user_id = get_jwt_identity()
    response, status_code = delete_sensor_service(sensor_id, user_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Sensor excluído com sucesso.", response)


@sensores_bp.route('/sensores/ultima', methods=['GET'])
@jwt_required()
def get_latest_sensor_data():
    tipo = request.args.get('tipo')
    tanque = request.args.get('tanque')
    user_id = get_jwt_identity()

    if not tipo or not tanque:
        return response_error("Os parâmetros 'tipo' e 'tanque' são obrigatórios.", 400)

    response, status_code = get_latest_sensor_data_service(tipo, tanque, user_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Último dado do sensor encontrado.", response)


@sensores_bp.route('/sensores/ultima/10', methods=['GET'])
@jwt_required()
def get_last_10_sensor_data():
    tipo = request.args.get('tipo')
    tanque = request.args.get('tanque')
    user_id = get_jwt_identity()

    if not tipo or not tanque:
        return response_error("Os parâmetros 'tipo' e 'tanque' são obrigatórios.", 400)

    response, status_code = get_last_10_sensor_data_service(tipo, tanque, user_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Últimos 10 dados do sensor encontrados.", response)
