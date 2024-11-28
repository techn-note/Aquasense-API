from database.db import mongo
from bson import ObjectId

class Atualizacao:
    @staticmethod
    def create_atualizacao(data):
        return mongo.db.atualizacoes.insert_one(data)
    
    @staticmethod
    def get_atualizacao(atualizacao_id):
        try:
            return mongo.db.atualizacoes.find_one({"_id": ObjectId(atualizacao_id)})
        except Exception:
            return None

    @staticmethod
    def get_all_atualizacoes():
        return mongo.db.atualizacoes.find()

    @staticmethod
    def update_atualizacao(atualizacao_id, update_data):
        try:
            return mongo.db.atualizacoes.update_one({"_id": ObjectId(atualizacao_id)}, {"$set": update_data})
        except Exception:
            return None

    @staticmethod
    def delete_atualizacao(atualizacao_id):
        try:
            return mongo.db.atualizacoes.delete_one({"_id": ObjectId(atualizacao_id)})
        except Exception:
            return None

    @staticmethod
    def get_latest_atualizacao(tanque):
        try:
            return mongo.db.atualizacoes.find({"tanque": tanque}).sort("data", -1).limit(1).next()
        except Exception:
            return None
