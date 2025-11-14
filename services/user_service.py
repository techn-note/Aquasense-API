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


def update_user_service(user_id, update_data):
    try:
        validated_data = user_schema.load(update_data, partial=True)
    except ValidationError as err:
        return {"error": err.messages}, 400

    if "email" in validated_data:
        existing_user = User.get_user_by_email(validated_data["email"])
        if existing_user and str(existing_user["_id"]) != str(user_id):
            return {"error": "E-mail já está sendo utilizado por outro usuário."}, 400

    if "password" in validated_data:
        validated_data["password"] = hash_password(validated_data["password"])

    updated = User.update_user(user_id, validated_data)

    if updated.matched_count == 0:
        return {"error": "Usuário não encontrado."}, 404

    return {"message": "Usuário atualizado com sucesso."}, 200


def get_user_profile_service(user_id):

    user = User.get_user(user_id)
    
    if not user:
        return {"error": "Usuário não encontrado"}, 404
    
    if 'password' in user:
        del user['password']
    
    if '_id' in user:
        user['_id'] = str(user['_id'])
    
    return user, 200