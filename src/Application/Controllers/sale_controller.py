from flask import request, jsonify, make_response
from flask_jwt_extended import get_jwt_identity
from src.Application.Service.sale_service import SaleService

class SaleController:
    @staticmethod
    def create_sale():
        data = request.get_json()
        seller_id = get_jwt_identity()

        product_id = data.get("product_id")
        quantity = data.get("quantity")

        if not product_id or not quantity:
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        sale_data = {
            "product_id": int(product_id),
            "quantity": int(quantity)
        }

        result = SaleService.create_sale(sale_data, seller_id)
        return result

    @staticmethod
    def list_sales():
        seller_id = get_jwt_identity()
        sales = SaleService.list_sales(seller_id)
        return make_response(jsonify({"vendas": sales}), 200)

    @staticmethod
    def inactivate_sale(id):
        # seller_id = get_jwt_identity()
        sale = SaleService.inactivate_sale(id)
        if sale == None:
            return make_response(jsonify({
                "mensagem": "Não existe Venda com esse ID"
            }), 404)
        return make_response(jsonify({
            "mensagem": "Venda inativada com sucesso"
        }), 200)