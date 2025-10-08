from database.db import mongo
from bson import ObjectId

class Sensor:
    @staticmethod
    def create_sensor(data):
        return mongo.db.sensores.insert_one(data)
    
    @staticmethod
    def get_sensor(sensor_id, user_id=None):
        query = {"_id": ObjectId(sensor_id)}
        if user_id:
            query["user_id"] = user_id
        return mongo.db.sensores.find_one(query)

    @staticmethod
    def get_all_sensores(user_id):
        return mongo.db.sensores.find({"user_id": user_id})

    @staticmethod
    def update_sensor(sensor_id, update_data, user_id=None):
        try:
            query = {"_id": ObjectId(sensor_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.sensores.update_one(query, {"$set": update_data})
        except Exception as e:
            print(f"Erro ao atualizar sensor: {e}")
            return None

    @staticmethod
    def delete_sensor(sensor_id, user_id=None):
        try:
            query = {"_id": ObjectId(sensor_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.sensores.delete_one(query)
        except Exception as e:
            print(f"Erro ao deletar sensor: {e}")
            return None

    @staticmethod
    def get_latest_sensor(tipo, tanque, user_id=None):
        query = {"tipo": tipo, "tanque": tanque}
        if user_id:
            query["user_id"] = user_id
        return mongo.db.sensores.find_one(query, sort=[("data", -1)])

    @staticmethod
    def get_last_10_sensor_data(tipo, tanque, user_id=None):
        pipeline = [
            {"$match": {"tipo": tipo, "tanque": tanque}},
            {"$sort": {"data": -1}},
            {"$limit": 10}
        ]
        if user_id:
            pipeline[0]["$match"]["user_id"] = user_id
        return list(mongo.db.sensores.aggregate(pipeline))
