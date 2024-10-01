from database.db import mongo

class Atualizacao:
    @staticmethod
    def create_atualizacao(data):
        return mongo.db.atualizacoes.insert_one(data)
    
    @staticmethod
    def get_atualizacao(atualizacao_id):
        return mongo.db.atualizacoes.find_one({"_id": atualizacao_id})

    @staticmethod
    def get_all_atualizacoes():
        return mongo.db.atualizacoes.find()

    @staticmethod
    def update_atualizacao(atualizacao_id, update_data):
        mongo.db.atualizacoes.update_one({"_id": atualizacao_id}, {"$set": update_data})

    @staticmethod
    def delete_atualizacao(atualizacao_id):
        mongo.db.atualizacoes.delete_one({"_id": atualizacao_id})
