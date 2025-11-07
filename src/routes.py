from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.product_controller import ProductController
from flask import jsonify, make_response
from flask_jwt_extended import jwt_required

def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    # Rotas referentes à users/sellers
    
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
    
    # Rotas referentes à products

    @app.route('/products', methods=['POST'])
    @jwt_required()
    def register_product():
        return ProductController.register_product()
    
    @app.route('/products', methods=['GET'])
    @jwt_required()
    def get_products():
        return ProductController.list_products()
    
    @app.route('/products/<int:id>', methods=['GET'])
    @jwt_required()
    def get_product_id(id):
        return ProductController.get_product(id)
    
    @app.route('/products/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_product(id):
        return ProductController.update_product(id)
    
    @app.route('/products/<int:id>', methods=['DELETE'])
    @jwt_required()
    def inactivate_product(id):
        return ProductController.inactivate_product(id)
    