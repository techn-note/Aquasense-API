from database.db import mongo
from bson.objectid import ObjectId

class Peixe:
    @staticmethod
    def create_peixe(data):
        return mongo.db.peixes.insert_one(data)
    
    @staticmethod
    def get_peixe(peixe_id):
        try:
            return mongo.db.peixes.find_one({"_id": ObjectId(peixe_id)})
        except Exception as e:
            print(f"Erro ao buscar peixe: {e}")
            return None
        
    @staticmethod
    def get_peixe_name(name):
        try:
            return mongo.db.peixes.find_one({"nome": name})
        except Exception as e:
            print(f"Erro ao buscar peixe: {e}")
            return None

    @staticmethod
    def get_all_peixes():
        try:
            return list(mongo.db.peixes.find())
        except Exception as e:
            print(f"Erro ao obter todos os peixes: {e}")
            return []

    @staticmethod
    def update_peixe(peixe_id, update_data):
        try:
            return mongo.db.peixes.update_one({"_id": ObjectId(peixe_id)}, {"$set": update_data})
        except Exception as e:
            print(f"Erro ao atualizar peixe: {e}")
            return None

    @staticmethod
    def delete_peixe(peixe_id):
        try:
            return mongo.db.peixes.delete_one({"_id": ObjectId(peixe_id)})
        except Exception as e:
            print(f"Erro ao deletar peixe: {e}")
            return None
