from database.db import mongo
from bson.objectid import ObjectId

class Tank:
    @staticmethod
    def create_tank(data):
        return mongo.db.tanks.insert_one(data)

    @staticmethod
    def get_all_tanks(user_id=None):
        query = {}
        if user_id:
            query["user_id"] = user_id
        return mongo.db.tanks.find(query)
    
    @staticmethod
    def get_tank(tank_id, user_id=None):
        try:
            query = {"_id": ObjectId(tank_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.tanks.find_one(query)
        except Exception as e:
            print(f"Erro ao buscar tanque: {e}")
            return None
        
    @staticmethod
    def get_tank_name(name, user_id=None):
        try:
            query = {"name": name}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.tanks.find_one(query)
        except Exception as e:
            print(f"Erro ao buscar tanque: {e}")
            return None

    @staticmethod
    def update_tank(tank_id, update_data, user_id=None):
        try:
            query = {"_id": ObjectId(tank_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.tanks.update_one(query, {"$set": update_data})
        except Exception as e:
            print(f"Erro ao atualizar tanque: {e}")
            return None

    @staticmethod
    def delete_tank(tank_id, user_id=None):
        try:
            query = {"_id": ObjectId(tank_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.tanks.delete_one(query)
        except Exception as e:
            print(f"Erro ao deletar tanque: {e}")
            return None
