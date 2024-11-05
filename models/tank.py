from database.db import mongo

class Tank:
    
    def create_tank(data):
        return mongo.db.tanks.insert_one(data)
    
    @staticmethod
    def get_all_tanks():
        return mongo.db.tanks.find()
    
    
    def update_tank(tank_id, update_data):
        mongo.db.tanks.update_one({"_id": tank_id}, {"$set": update_data})
    
    @staticmethod
    def delete_tank(tank_id):
        mongo.db.tanks.update_one({"_id": tank_id})