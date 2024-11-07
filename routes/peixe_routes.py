from flask import Blueprint, request
from services.peixe_service import (
    create_peixe_service,
    get_peixe_service,
    get_all_peixes_service,
    update_peixe_service,
    delete_peixe_service
)
from utils.helpers import response_success, response_error

peixe_bp = Blueprint('peixe', __name__)

@peixe_bp.route('/peixes', methods=['POST'])
def add_peixe():
    data = request.get_json()
    response, status_code = create_peixe_service(**data)
    
    if status_code != 201:
        return response_error(response, status_code)
    
    return response_success("Peixe foi adicionado com sucesso.", response)

@peixe_bp.route('/peixes/<string:peixe_id>', methods=['GET'])
def get_peixe(peixe_id):
    response, status_code = get_peixe_service(peixe_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Peixe encontrado.", response)

@peixe_bp.route('/peixes', methods=['GET'])
def get_all_peixes():
    response = get_all_peixes_service()
    return response_success("Lista de peixes retornada com sucesso.", response)

@peixe_bp.route('/peixes/<string:peixe_id>', methods=['PUT'])
def update_peixe(peixe_id):
    data = request.get_json()
    response, status_code = update_peixe_service(peixe_id, data)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Peixe atualizado com sucesso.", response)


@peixe_bp.route('/peixes/<string:peixe_id>', methods=['DELETE'])
def delete_peixe(peixe_id):
    response, status_code = delete_peixe_service(peixe_id)
    
    if status_code != 200:
        return response_error(response, status_code)
    
    return response_success("Peixe deletado com sucesso.", response)
