from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService

class ProductController:
    @staticmethod
    def register_product():
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        quantity = data.get('quantity')
        image = data.get('image')

        if not name or not price or not quantity:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        product_data = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "image": image
        }

        product = ProductService.create_product(product_data)

        return make_response(jsonify({
            "mensagem": "Produto salvo com sucesso",
            "usuarios": product.to_dict()
        }), 200)
    
    @staticmethod
    def list_products():
        products = ProductService.list_products()
        return make_response(jsonify({
            "products": products
        }), 200)

    @staticmethod
    def get_product(id):
        product = ProductService.get_product(id)
        return product

    @staticmethod
    def update_product(id):
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Missing update data"}), 400)
        
        updated_product = ProductService.update_product(id, data)
        return make_response(jsonify({
            "mensagem": "Produto atualizado com sucesso",
            "produto": updated_product
        }), 200)

    @staticmethod
    def inactave_product(id):
        product = ProductService.inactave_product(id)
        if product == None:
            return make_response(jsonify({
                "mensagem": "Não existe Produto com esse ID"
            }))
        return make_response(jsonify({
            "mensagem": "Produto deletado com sucesso"
        }), 200)