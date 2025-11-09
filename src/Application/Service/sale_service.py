from src.Domain.sale import SaleDomain
from src.Infrastructure.Model.sale import Sale
from src.Infrastructure.Model.product import Product
from src.config.data_base import db
from flask import jsonify, make_response

class SaleService:
    @staticmethod
    def create_sale(sale_data, seller_id):
        product = Product.query.get(sale_data["product_id"])

        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)

        if not product.status:
            return make_response(jsonify({"erro": "Produto inativo, não pode ser vendido"}), 400)

        if product.seller_id != int(seller_id):
            return make_response(jsonify({"erro": "Você não tem permissão para vender este produto"}), 403)

        if product.quantity < sale_data["quantity"]:
            return make_response(jsonify({"erro": "Quantidade insuficiente em estoque"}), 400)

        new_sale = SaleDomain(
            product_id=sale_data["product_id"],
            quantity=sale_data["quantity"],
            price_at_sale=product.price
        )

        sale = Sale(
            product_id=new_sale.product_id,
            quantity=new_sale.quantity,
            price_at_sale=new_sale.price_at_sale
        )

        product.quantity -= new_sale.quantity

        db.session.add(sale)
        db.session.commit()

        return sale.to_dict()

    @staticmethod
    def list_sales(seller_id):
        sales = Sale.query.join(Product).filter(Product.seller_id == int(seller_id)).order_by(Sale.created_at.desc()).all()
        sale_list = []

        for sale in sales:
            sale_list.append(sale.to_dict())
        
        return sale_list
