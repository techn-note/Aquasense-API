from flask import Flask
from routes.routes import routes
from database.db import initialize_db
from extensions.extensions import Extensions
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

initialize_db(app)

Extensions.initialize_jwt(app)
Extensions.initialize_marsh(app)
Extensions.initialize_bcript(app)


app.register_blueprint(routes)


if __name__ == '__main__':
    app.run(debug=True)
