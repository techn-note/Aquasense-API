from database.db import mongo

class Sensor:
    @staticmethod
    def create_sensor(data):
        return mongo.db.sensores.insert_one(data)
    
    @staticmethod
    def get_sensor(sensor_id):
        return mongo.db.sensores.find_one({"_id": sensor_id})

    @staticmethod
    def get_all_sensores():
        return mongo.db.sensores.find()

    @staticmethod
    def update_sensor(sensor_id, update_data):
        mongo.db.sensores.update_one({"_id": sensor_id}, {"$set": update_data})

    @staticmethod
    def delete_sensor(sensor_id):
        mongo.db.sensores.delete_one({"_id": sensor_id})
