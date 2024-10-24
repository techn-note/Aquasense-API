from models.sensores import Sensor
from schemas.sensores_schema import SensorSchema
from marshmallow import ValidationError
from datetime import datetime

sensor_schema = SensorSchema()

def create_sensor_service(tipo, data, valor, tanque):
    # Dados do sensor recebidos
    sensor_data = {
        "tipo": tipo,
        "data": data,
        "valor": valor,
        "tanque": tanque
    }

    try:
        validated_data = sensor_schema.load(sensor_data)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    result = Sensor.create_sensor(validated_data)
    return {"sensor_id": str(result.inserted_id)}, 201

def get_sensor_service(sensor_id):
    sensor = Sensor.get_sensor(sensor_id)
    
    if not sensor:
        return {"error": "Sensor not found"}, 404
    
    return sensor_schema.dump(sensor), 200

def get_all_sensores_service():
    sensores = Sensor.get_all_sensores()
    
    return sensor_schema.dump(sensores, many=True), 200

def update_sensor_service(sensor_id, update_data):

    try:
        validated_data = sensor_schema.load(update_data, partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400

    updated = Sensor.update_sensor(sensor_id, validated_data)
    
    if updated.matched_count == 0:
        return {"error": "Sensor not found"}, 404
    
    return {"message": "Sensor updated successfully"}, 200

def delete_sensor_service(sensor_id):
    deleted = Sensor.delete_sensor(sensor_id)
    
    if deleted.deleted_count == 0:
        return {"error": "Sensor not found"}, 404
    
    return {"message": "Sensor deleted successfully"}, 200
