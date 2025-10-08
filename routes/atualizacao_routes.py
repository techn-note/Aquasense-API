from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.atualizacao_service import (
    create_atualizacao_service,
    get_atualizacao_service,
    get_all_atualizacoes_service,
    update_atualizacao_service,
    delete_atualizacao_service,
    get_latest_atualizacao_service
)
from utils.helpers import response_success, response_error

atualizacao_bp = Blueprint('atualizacao', __name__)

@atualizacao_bp.route('/atualizacoes', methods=['POST'])
@jwt_required()
def add_atualizacao():
    user_id = get_jwt_identity()
    tanque = request.args.get('tanque')
    
    if not tanque:
        return response_error({"error": "Tanque não especificado"}, 400)
    
    response, status_code = create_atualizacao_service(tanque, user_id)
    
    if status_code != 201:
        return response_error(response, status_code)
    
    return response_success("Atualização foi adicionada com sucesso.", response)


@atualizacao_bp.route('/atualizacoes/<string:atualizacao_id>', methods=['GET'])
@jwt_required()
def get_atualizacao(atualizacao_id):
    user_id = get_jwt_identity()
    response, status_code = get_atualizacao_service(atualizacao_id, user_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Atualização encontrada.", response)


@atualizacao_bp.route('/atualizacoes', methods=['GET'])
@jwt_required()
def get_all_atualizacoes():
    user_id = get_jwt_identity()
    response, status_code = get_all_atualizacoes_service(user_id)
    return response_success("Lista de atualizações retornada com sucesso.", response)


@atualizacao_bp.route('/atualizacoes/<string:atualizacao_id>', methods=['PUT'])
@jwt_required()
def update_atualizacao(atualizacao_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    response, status_code = update_atualizacao_service(atualizacao_id, data, user_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Atualização feita com sucesso.", response)


@atualizacao_bp.route('/atualizacoes/<string:atualizacao_id>', methods=['DELETE'])
@jwt_required()
def delete_atualizacao(atualizacao_id):
    user_id = get_jwt_identity()
    response, status_code = delete_atualizacao_service(atualizacao_id, user_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Atualização deletada com sucesso.", response)


@atualizacao_bp.route('/atualizacoes/ultima', methods=['GET'])
@jwt_required()
def get_latest_atualizacao():
    user_id = get_jwt_identity()
    tanque = request.args.get('tanque')
    
    if not tanque:
        return response_error({"error": "Tanque não especificado"}, 400)
    
    response, status_code = get_latest_atualizacao_service(tanque, user_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Última atualização encontrada.", response)
