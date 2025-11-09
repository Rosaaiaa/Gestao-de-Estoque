from src.config.data_base import db
from src.Infrastructure.Model.sale import Sale
from src.Infrastructure.Model.product import Product
from sqlalchemy import func

class ReportService:
    @staticmethod
    def get_sales_by_product(seller_id):
        sales_list = []
        results = (
            db.session.query(
                Product.name.label("product_name"),
                func.sum(Sale.quantity).label("total_sold")
            )
            .join(Sale, Product.id == Sale.product_id)
            .filter(Product.seller_id == int(seller_id))
            .group_by(Product.id)
            .order_by(func.sum(Sale.quantity).desc())
            .all()
        )

        for sale in results:
            sales_list.append(
                {
                    "product_name": sale.product_name, 
                    "total_sold": int(sale.total_sold)
                })
            
        return sales_list

    @staticmethod
    def get_top_products(seller_id):
        products_list = []
        results = (
            db.session.query(
                Product.name.label("product_name"),
                func.sum(Sale.price_at_sale * Sale.quantity).label("total_revenue")
            )
            .join(Sale, Product.id == Sale.product_id)
            .filter(Product.seller_id == int(seller_id))
            .group_by(Product.id)
            .order_by(func.sum(Sale.price_at_sale * Sale.quantity).desc())
            .limit(3)
            .all()
        )

        for product in results:
            products_list.append(
                {
                    "product_name": product.product_name, 
                    "total_revenue": float(product.total_revenue)
                })
            
        return products_list
