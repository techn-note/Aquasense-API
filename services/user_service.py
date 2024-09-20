from models.user import User
from schemas.user_schema import UserSchema
from utils.helpers import hash_password, validate_login
from marshmallow import ValidationError

user_schema = UserSchema()

def create_user_service(name, email, age, country, password):
    user_data = {
        "name": name,
        "email": email,
        "age": age,
        "country": country,
        "password": password
    }
    
    try:
        validated_data = user_schema.load(user_data)
    except ValidationError as err:
        return {"error": err.messages}, 400
    
    validated_data['password'] = hash_password(validated_data['password'])

    result = User.create_user(validated_data)
    return {"user_id": str(result.inserted_id)}, 201


def loged(email, password):
    return validate_login(email, password)