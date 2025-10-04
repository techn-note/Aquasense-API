from database.db import mongo
from bson import ObjectId

class Atualizacao:
    @staticmethod
    def create_atualizacao(data):
        return mongo.db.atualizacoes.insert_one(data)

    @staticmethod
    def get_atualizacao(atualizacao_id, user_id=None):
        try:
            query = {"_id": ObjectId(atualizacao_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.atualizacoes.find_one(query)
        except Exception:
            return None

    @staticmethod
    def get_all_atualizacoes(user_id):
        return list(mongo.db.atualizacoes.find({"user_id": user_id}))

    @staticmethod
    def update_atualizacao(atualizacao_id, update_data, user_id=None):
        try:
            query = {"_id": ObjectId(atualizacao_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.atualizacoes.update_one(query, {"$set": update_data})
        except Exception:
            return None

    @staticmethod
    def delete_atualizacao(atualizacao_id, user_id=None):
        try:
            query = {"_id": ObjectId(atualizacao_id)}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.atualizacoes.delete_one(query)
        except Exception:
            return None

    @staticmethod
    def get_latest_atualizacao(tanque, user_id=None):
        try:
            query = {"tanque": tanque}
            if user_id:
                query["user_id"] = user_id
            return mongo.db.atualizacoes.find(query).sort("data", -1).limit(1).next()
        except Exception:
            return None
