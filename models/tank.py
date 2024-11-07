from database.db import mongo
from bson.objectid import ObjectId

class Tank:
    @staticmethod
    def create_tank(data):
        return mongo.db.tanks.insert_one(data)

    @staticmethod
    def get_all_tanks():
        return mongo.db.tanks.find()
    
    @staticmethod
    def get_tank(tank_id):
        try:
            return mongo.db.tanks.find_one({"_id": ObjectId(tank_id)})
        except Exception as e:
            print(f"Erro ao buscar tanque: {e}")
            return None

    @staticmethod
    def update_tank(tank_id, update_data):
        try:
            return mongo.db.tanks.update_one({"_id": ObjectId(tank_id)}, {"$set": update_data})
        except Exception as e:
            print(f"Erro ao atualizar tanque: {e}")
            return None

    @staticmethod
    def delete_tank(tank_id):
        try:
            return mongo.db.tanks.delete_one({"_id": ObjectId(tank_id)})
        except Exception as e:
            print(f"Erro ao deletar tanque: {e}")
            return None
