from flask import Blueprint
from routes.user_routes import user_bp
from routes.tank_routes import tank_bp

routes = Blueprint('routes', __name__)

routes.register_blueprint(user_bp)
routes.register_blueprint(tank_bp)