from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService
from flask_jwt_extended import get_jwt_identity
from src.Infrastructure.http.upload_image import upload_product_image

class ProductController:
    @staticmethod
    def register_product():
        name = request.form.get('name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        image_file = request.files.get('image')

        image_url = None
        if image_file:
            image_url = upload_product_image(image_file, get_jwt_identity())

        if not name or price is None or quantity is None:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        product_data = {
            "name": name,
            "price": float(price),
            "quantity": int(quantity),
            "image": image_url
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
        name = request.form.get('name')
        price = request.form.get('price')
        quantity = request.form.get('quantity')
        image_file = request.files.get('image')

        seller_id = get_jwt_identity()

        existing_product = ProductService.get_product(id, seller_id)
        if not existing_product:
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

        image_url = existing_product['image']
        if image_file:
            image_url = upload_product_image(image_file, seller_id)

        product_data = {
            "name": name if name else existing_product['name'],
            "price": float(price) if price else existing_product['price'],
            "quantity": int(quantity) if quantity else existing_product['quantity'],
            "image": image_url
        }

        updated_product = ProductService.update_product(id, product_data, seller_id, image_url)

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
            "mensagem": "Produto inativado com sucesso"
        }), 200)