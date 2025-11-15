from flask import Flask, request, jsonify
from routes.routes import routes
from database.db import initialize_db
from extensions.extensions import Extensions
from config import Config
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

CORS(app)

print()

app.config.from_object(Config)

initialize_db(app)
Extensions.initialize_jwt(app)
Extensions.initialize_marsh(app)
Extensions.initialize_bcript(app)

app.register_blueprint(routes)

# URL da API Neural Network (configurável via variável de ambiente)
NEURAL_API_URL = os.getenv('NEURAL_API_URL', 'http://localhost:8000')


@app.route('/neural-predict', methods=['POST'])
def neural_predict():
    """Rota que encaminha requisições para a Neural Network API."""
    data = request.get_json()
    try:
        response = requests.post(
            f'{NEURAL_API_URL}/predict',
            json=data,
            timeout=10
        )
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({
            'error': 'Erro ao conectar com a API de predição neural',
            'details': str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
