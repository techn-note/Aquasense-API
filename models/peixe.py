from database.db import mongo

class Peixe:
    @staticmethod
    def create_peixe(data):
        return mongo.db.peixes.insert_one(data)
    
    @staticmethod
    def get_peixe(peixe_id):
        return mongo.db.peixes.find_one({"_id": peixe_id})

    @staticmethod
    def get_all_peixes():
        return mongo.db.peixes.find()

    @staticmethod
    def update_peixe(peixe_id, update_data):
        mongo.db.peixes.update_one({"_id": peixe_id}, {"$set": update_data})

    @staticmethod
    def delete_peixe(peixe_id):
        mongo.db.peixes.delete_one({"_id": peixe_id})
