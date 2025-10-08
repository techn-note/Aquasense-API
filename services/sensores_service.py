from models.sensores import Sensor
from schemas.sensores_schema import SensorSchema
from marshmallow import ValidationError

sensor_schema = SensorSchema()

def create_sensor_service(tipo, data, valor, tanque, user_id):
    sensor_data = {
        "tipo": tipo,
        "data": data,
        "valor": valor,
        "tanque": tanque,
        "user_id": user_id
    }

    try:
        validated_data = sensor_schema.load(sensor_data)
    except ValidationError as err:
        return {"error": err.messages}, 400

    result = Sensor.create_sensor(validated_data)
    return {"sensor_id": str(result.inserted_id)}, 201


def get_sensor_service(sensor_id, user_id):
    sensor = Sensor.get_sensor(sensor_id, user_id=user_id)

    if not sensor:
        return {"error": "Sensor não encontrado"}, 404

    return sensor_schema.dump(sensor), 200


def get_all_sensores_service(user_id):
    sensores = Sensor.get_all_sensores(user_id=user_id)
    return sensor_schema.dump(sensores, many=True), 200


def update_sensor_service(sensor_id, update_data, user_id):
    try:
        validated_data = sensor_schema.load(update_data, partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400

    updated = Sensor.update_sensor(sensor_id, validated_data, user_id=user_id)

    if updated.matched_count == 0:
        return {"error": "Sensor não encontrado"}, 404

    return {"message": "Sensor atualizado com sucesso"}, 200


def delete_sensor_service(sensor_id, user_id):
    deleted = Sensor.delete_sensor(sensor_id, user_id=user_id)

    if deleted.deleted_count > 0:
        return {"message": "Sensor deletado com sucesso"}, 200
    else:
        return {"error": "Sensor não encontrado"}, 404


def get_latest_sensor_data_service(tipo, tanque, user_id):
    sensor = Sensor.get_latest_sensor(tipo, tanque, user_id=user_id)

    if not sensor:
        return {"error": "Nenhum registro encontrado para este tipo ou tanque"}, 404

    return sensor_schema.dump(sensor), 200


def get_last_10_sensor_data_service(tipo, tanque, user_id):
    try:
        sensores = Sensor.get_last_10_sensor_data(tipo, tanque, user_id=user_id)
        if not sensores:
            return {"error": "Nenhum registro encontrado para este tipo e tanque"}, 404

        return sensor_schema.dump(sensores, many=True), 200
    except Exception as e:
        return {"error": str(e)}, 500
