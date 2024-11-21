from database.db import mongo
from bson import ObjectId

class User:
    @staticmethod
    def create_user(data):
        return mongo.db.users.insert_one(data)


    @staticmethod
    def get_user(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})


    @staticmethod
    def get_user_by_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def update_user(user_id, update_data):
        mongo.db.users.update_one({"_id": user_id}, {"$set": update_data})

    @staticmethod
    def delete_user(user_id):
        mongo.db.users.delete_one({"_id": user_id})
