from models.tank import Tank
from schemas.tank_schema import TankSchema
from marshmallow import ValidationError

tank_schema = TankSchema()

def create_tank_service(name, capacity, number, user_id):
    tank_data = {
        "name": name,
        "capacity": capacity,
        "number": number,
        "user_id": user_id
    }
    
    try:
        validated_data = tank_schema.load(tank_data)
    except ValidationError as err:
        return {"error": err.messages}, 400

    result = Tank.create_tank(validated_data)
    return {"tank_id": str(result.inserted_id)}, 201


def get_tank_service(tank_id, user_id):
    tank = Tank.get_tank(tank_id, user_id=user_id)
    
    if not tank:
        return {"error": "Tank não encontrado"}, 404
    
    return tank_schema.dump(tank), 200


def get_tank_service_name(name, user_id):
    try:
        tank = Tank.get_tank_name(name, user_id=user_id)
        if not tank:
            return {"error": "Tank não encontrado"}, 404
        
        tank_data = tank_schema.dump(tank)
        tank_data['_id'] = str(tank.get('_id'))
        return tank_data, 200
    except Exception as e:
        return {"error": f"Erro ao buscar tanque: {str(e)}"}, 500


def get_all_tanks_service(user_id):
    tanks = Tank.get_all_tanks(user_id=user_id)
    return tank_schema.dump(tanks, many=True), 200


def update_tank_service(tank_id, update_data, user_id):
    try:
        validated_data = tank_schema.load(update_data, partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400

    updated = Tank.update_tank(tank_id, validated_data, user_id=user_id)
    
    if updated.matched_count == 0:
        return {"error": "Tank não encontrado"}, 404
    
    return {"message": "Tank atualizado com sucesso"}, 200


def delete_tank_service(tank_id, user_id):
    deleted = Tank.delete_tank(tank_id, user_id=user_id)
    
    if deleted.deleted_count > 0:
        return {"message": "Tank deletado com sucesso"}, 200
    else:
        return {"error": "Tank não encontrado"}, 404
