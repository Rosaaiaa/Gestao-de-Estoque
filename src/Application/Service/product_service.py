from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.config.data_base import db

class ProductService:
    @staticmethod
    def create_product(product_data):
        new_product = ProductDomain(
            name=product_data['name'],
            price=product_data['price'],
            quantity=product_data['quantity'],
            image=product_data['image']
        )
        
        product = Product(
            name=new_product.name,
            price=new_product.price,
            quantity=new_product.quantity,
            image=new_product.image,
            status=new_product.status
        )
        db.session.add(product)
        db.session.commit()
        
        return product
    
    @staticmethod
    def list_products():
        products = Product.query.all()
        product_list = []
        for product in products:
            product_list.append(product.to_dict())
        return product_list
    
    @staticmethod
    def get_product(id):
        product = Product.query.get(id)
        return product.to_dict()

    @staticmethod
    def update_product(id, data):
        product = Product.query.get(id)
        for chave, valor in data.items():
            setattr(product, chave, valor)

        db.session.commit()
        return product.to_dict()
    
    @staticmethod
    def inactave_product(id):
        product = Product.query.get(id)
        if not product:
            return None
        product.status = False
        db.session.commit()
        return product.to_dict()