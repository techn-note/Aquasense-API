from flask import Blueprint, request
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

sensores_bp = Blueprint('sensores', __name__)

@sensores_bp.route('/sensores', methods=['POST'])
def add_sensor():
    data = request.get_json()
    response, status_code = create_sensor_service(**data)

    if status_code != 201:
        return response_error(response, status_code)

    return response_success("Sensor foi adicionado com sucesso.", {"id": response})


@sensores_bp.route('/sensores/<string:sensor_id>', methods=['GET'])
def get_sensor(sensor_id):
    response, status_code = get_sensor_service(sensor_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Sensor encontrado.", response)

@sensores_bp.route('/sensores', methods=['GET'])
def get_all_sensores():
    response, status_code = get_all_sensores_service()
    return response_success("Sensores encontrados.", response)

@sensores_bp.route('/sensores/<string:sensor_id>', methods=['PUT'])
def update_sensor(sensor_id):
    data = request.get_json()
    response, status_code = update_sensor_service(sensor_id, data)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Sensor atualizado com sucesso.", response)

@sensores_bp.route('/sensores/<string:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    response, status_code = delete_sensor_service(sensor_id)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Sensor excluído com sucesso.", response)

@sensores_bp.route('/sensores/latest', methods=['GET'])
def get_latest_sensor_data():
    tipo = request.args.get('tipo')
    tanque = request.args.get('tanque')

    if not tipo or not tanque:
        return response_error("Os parâmetros 'tipo' e 'tanque' são obrigatórios.", 400)

    response, status_code = get_latest_sensor_data_service(tipo, tanque)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Último dado do sensor encontrado.", response)


@sensores_bp.route('/sensores/latest/10', methods=['GET'])
def get_last_10_sensor_data():
    tipo = request.args.get('tipo')
    tanque = request.args.get('tanque')

    if not tipo or not tanque:
        return response_error("Os parâmetros 'tipo' e 'tanque' são obrigatórios.", 400)

    response, status_code = get_last_10_sensor_data_service(tipo, tanque)

    if status_code != 200:
        return response_error(response, status_code)

    return response_success("Últimos 10 dados do sensor encontrados.", response)
