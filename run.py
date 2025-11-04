from flask import Flask
from flask_cors import CORS
from src.config.data_base import init_db, db
from src.routes import init_routes
from flask_jwt_extended import JWTManager
import os

def create_app():
    """
    Função que cria e configura a aplicação Flask.
    """
    app = Flask(__name__)

    CORS(app, origins=['https://react-gestao-de-estoque.vercel.app/'])

    init_db(app)
    init_routes(app)

    app.config["JWT_SECRET_KEY"] = "e999c435-6b35-4c11-89f3-efe62dd15f08"

    return app

app = create_app()
jwt = JWTManager(app)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
