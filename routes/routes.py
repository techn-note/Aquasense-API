from flask import Blueprint
from routes.user_routes import user_bp
from routes.tank_routes import tank_bp
from routes.peixe_routes import peixe_bp
from routes.atualizacao_routes import atualizacao_bp
from routes.sensores_routes import sensores_bp

routes = Blueprint('routes', __name__)

routes.register_blueprint(user_bp)
routes.register_blueprint(tank_bp)
routes.register_blueprint(peixe_bp)
routes.register_blueprint(atualizacao_bp)
routes.register_blueprint(sensores_bp)

