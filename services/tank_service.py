from models.tank import Tank
from schemas.tank_schema import TankSchema
from marshmallow import ValidationError

tank_schema = TankSchema()

def create_tank_service(name, capacity, number):
    tank_data = {
        "name": name,
        "capacity": capacity,
        "number": number
    }
    
    result = Tank.create_tank(tank_data)

    return {"message": "Tank created successfully", "tank_id": str(result.inserted_id)}, 201

def get_tank_service(tank_id):
    tank = Tank.get_tank(tank_id)
    
    if not tank:
        return {"error": "Tank not found"}, 404
    
    return tank_schema.dump(tank), 200

def get_tank_service_name(name):
    try:
        tank = Tank.get_tank_name(name)
        
        if not tank:
            return {"error": "Tank not found"}, 404
        
        return tank_schema.dump(tank), 200
    except Exception as e:
        return {"error": f"Erro ao buscar tanque: {str(e)}"}, 500


def get_all_tanks_service():
    tanks = Tank.get_all_tanks()
    return tank_schema.dump(tanks, many=True), 200

def update_tank_service(tank_id, update_data):
    try:
        validated_data = tank_schema.load(update_data, partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400

    updated = Tank.update_tank(tank_id, validated_data)
    
    if updated.matched_count == 0:
        return {"error": "Tank not found"}, 404
    
    return {"message": "Tank updated successfully"}, 200

def delete_tank_service(tank_id):
    deleted = Tank.delete_tank(tank_id)
    
    if deleted.deleted_count > 0:
        return {"message": "Tanque Deletado com Sucesso"}, 200
    else:
        return {"error": "Tanque não encontrado"}, 404
