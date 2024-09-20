from flask import jsonify
from extensions.extensions import bcrypt

def response_success(message, data=None):
    return jsonify({"message": message, "data": data}), 200

def response_error(message, status_code=400):
    return jsonify({"error": message}), status_code

def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password_hash(hashed_password_hash, plain_password):
    return bcrypt.check_password_hash(hashed_password_hash, plain_password)

def validate_login(email, password):
    from models.user import User
    from flask_jwt_extended import create_access_token
    
    user = User.get_user_by_email(email)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=str(user['_id']))
        return access_token
    return None

