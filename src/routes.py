from src.Application.Controllers.user_controller import UserController
from flask import jsonify, make_response
from flask_jwt_extended import jwt_required

def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    @app.route('/user/ativacao', methods=['POST'])
    def ativacao_user():
        return UserController.ativacao()
    
    @app.route('/user', methods=['GET'])
    @jwt_required()
    def get_users():
        return UserController.list_users()
    
    @app.route('/user/<int:id>', methods=['GET'])
    @jwt_required()
    def get_user_id(id):
        return UserController.get_user(id)
    
    @app.route('/user/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_user(id):
        return UserController.update_user(id)
    
    @app.route('/user/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_user(id):
        return UserController.delete_user(id)
    
    @app.route('/login', methods=['POST'])
    def login():
        return UserController.login()