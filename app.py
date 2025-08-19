from flask import Flask, request, jsonify
from routes.routes import routes
from database.db import initialize_db
from extensions.extensions import Extensions
from config import Config
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

print()

app.config.from_object(Config)  # <- Isso já usa a URI fixa

initialize_db(app)
Extensions.initialize_jwt(app)
Extensions.initialize_marsh(app)
Extensions.initialize_bcript(app)

app.register_blueprint(routes)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        response = requests.post('http://localhost:8001/predict', json=data, timeout=10)
        response.raise_for_status()
        return jsonify(response.json()), response.status_code
    except requests.RequestException as e:
        return jsonify({'error': 'Erro ao conectar com a API de predição', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
