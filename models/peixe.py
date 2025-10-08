from database.db import mongo
from bson.objectid import ObjectId

class Peixe:
    @staticmethod
    def create_peixe(data):
        return mongo.db.peixes.insert_one(data)
    
    @staticmethod
    def get_peixe(peixe_id, user_id=None):
        try:
            query = {"_id": ObjectId(peixe_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.peixes.find_one(query)
        except Exception as e:
            print(f"Erro ao buscar peixe: {e}")
            return None
        
    @staticmethod
    def get_peixe_name(name, user_id=None):
        try:
            query = {"nome": name}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.peixes.find_one(query)
        except Exception as e:
            print(f"Erro ao buscar peixe: {e}")
            return None

    @staticmethod
    def get_all_peixes(user_id):
        try:
            return list(mongo.db.peixes.find({"user_id": user_id}))
        except Exception as e:
            print(f"Erro ao obter todos os peixes: {e}")
            return []

    @staticmethod
    def update_peixe(peixe_id, update_data, user_id=None):
        try:
            query = {"_id": ObjectId(peixe_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.peixes.update_one(query, {"$set": update_data})
        except Exception as e:
            print(f"Erro ao atualizar peixe: {e}")
            return None

    @staticmethod
    def delete_peixe(peixe_id, user_id=None):
        try:
            query = {"_id": ObjectId(peixe_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.peixes.delete_one(query)
        except Exception as e:
            print(f"Erro ao deletar peixe: {e}")
            return None
