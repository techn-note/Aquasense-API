from database.db import mongo
from bson.objectid import ObjectId

class Sensor:
    @staticmethod
    def create_sensor(data):
        return mongo.db.sensores.insert_one(data)
    
    @staticmethod
    def get_sensor(sensor_id):
        return mongo.db.sensores.find_one({"_id": ObjectId(sensor_id)})

    @staticmethod
    def get_all_sensores():
        return mongo.db.sensores.find()

    @staticmethod
    def update_sensor(sensor_id, update_data):
        try:
            return mongo.db.sensores.update_one({"_id": ObjectId(sensor_id)}, {"$set": update_data})
        except Exception as e:
            print(f"Erro ao atualizar sensor: {e}")
            return None

    @staticmethod
    def delete_sensor(sensor_id):
        try:
            return mongo.db.sensores.delete_one({"_id": ObjectId(sensor_id)})
        except Exception as e:
            print(f"Erro ao deletar sensor: {e}")
            return None

    @staticmethod
    def get_latest_sensor(tipo, tanque):
        return mongo.db.sensores.find_one(
            {"tipo": tipo, "tanque": tanque},
            sort=[("data", -1)]
        )

    @staticmethod
    def get_last_10_sensor_data(tipo, tanque):
        pipeline = [
            {"$match": {"tipo": tipo, "tanque": tanque}},
            {"$sort": {"data": -1}},
            {"$limit": 5}
        ]
        return list(mongo.db.sensores.aggregate(pipeline))

