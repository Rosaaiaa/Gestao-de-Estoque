from flask import jsonify, make_response
from src.Application.Service.report_service import ReportService
from flask_jwt_extended import get_jwt_identity

class ReportController:
    @staticmethod
    def sales_by_product():
        seller_id = get_jwt_identity()
        data = ReportService.get_sales_by_product(seller_id)
        return make_response(jsonify(data), 200)

    @staticmethod
    def top_products():
        seller_id = get_jwt_identity()
        data = ReportService.get_top_products(seller_id)
        return make_response(jsonify(data), 200)
