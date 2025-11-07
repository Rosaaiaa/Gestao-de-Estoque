from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService
from flask_jwt_extended import get_jwt_identity

class ProductController:
    @staticmethod
    def register_product():
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        quantity = data.get('quantity')
        image = data.get('image')

        if not name or price is None or quantity is None:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        product_data = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "image": image
        }

        seller_id = get_jwt_identity()
        product = ProductService.create_product(product_data, seller_id)

        return make_response(jsonify({
            "mensagem": "Produto salvo com sucesso",
            "produtos": product.to_dict()
        }), 200)
    
    @staticmethod
    def list_products():
        seller_id = get_jwt_identity()
        products = ProductService.list_products(seller_id)
        return make_response(jsonify({
            "produtos": products
        }), 200)

    @staticmethod
    def get_product(id):
        seller_id = get_jwt_identity()
        product = ProductService.get_product(id, seller_id)
        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)
        return make_response(jsonify(product), 200)

    @staticmethod
    def update_product(id):
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Missing update data"}), 400)
        
        seller_id = get_jwt_identity()
        updated_product = ProductService.update_product(id, data, seller_id)
        if not updated_product:
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)
        
        return make_response(jsonify({
            "mensagem": "Produto atualizado com sucesso",
            "produto": updated_product
        }), 200)

    @staticmethod
    def inactivate_product(id):
        seller_id = get_jwt_identity()
        product = ProductService.inactivate_product(id, seller_id)
        if product == None:
            return make_response(jsonify({
                "mensagem": "Não existe Produto com esse ID"
            }), 404)
        return make_response(jsonify({
            "mensagem": "Produto deletado com sucesso"
        }), 200)