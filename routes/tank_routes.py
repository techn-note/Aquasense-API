from flask import Blueprint, request
from services.tank_service import create_tank_service
from utils.helpers import response_success

tank_bp = Blueprint('tank', __name__)

@tank_bp.route('/tanks', methods=['POST'])
def add_tank():
    data = request.get_json()
    
    tank_id = create_tank_service(**data)
    return response_success("Tanque adicionado com sucesso!", {"tank_id": tank_id})