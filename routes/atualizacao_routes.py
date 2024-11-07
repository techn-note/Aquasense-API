from flask import Blueprint, request
from services.atualizacao_service import (
    create_atualizacao_service,
    get_atualizacao_service,
    get_all_atualizacoes_service,
    update_atualizacao_service,
    delete_atualizacao_service
)
from utils.helpers import response_success, response_error

atualizacao_bp = Blueprint('atualizacao', __name__)

@atualizacao_bp.route('/atualizacoes', methods=['POST'])
def add_atualizacao():
    data = request.get_json()
    response, status_code = create_atualizacao_service(**data)
    
    if status_code != 201:
        return response_error(response, status_code)
    
    return response_success("Atualização foi adicionada com sucesso.", response)


@atualizacao_bp.route('/atualizacoes/<string:atualizacao_id>', methods=['GET'])
def get_atualizacao(atualizacao_id):
    response, status_code = get_atualizacao_service(atualizacao_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Atualização encontrada.", response)


@atualizacao_bp.route('/atualizacoes', methods=['GET'])
def get_all_atualizacoes():
    response = get_all_atualizacoes_service()
    return response_success("Lista de atualizações retornada com sucesso.", response)


@atualizacao_bp.route('/atualizacoes/<string:atualizacao_id>', methods=['PUT'])
def update_atualizacao(atualizacao_id):
    data = request.get_json()
    response, status_code = update_atualizacao_service(atualizacao_id, data)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Atualização feita com sucesso.", response)


@atualizacao_bp.route('/atualizacoes/<string:atualizacao_id>', methods=['DELETE'])
def delete_atualizacao(atualizacao_id):
    response, status_code = delete_atualizacao_service(atualizacao_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Atualização deletada com sucesso.", response)
