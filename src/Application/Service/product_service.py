from src.Domain.product import ProductDomain
from src.Infrastructure.Model.product import Product
from src.config.data_base import db

class ProductService:
    @staticmethod
    def create_product(product_data, seller_id):
        new_product = ProductDomain(
            name=product_data['name'],
            price=product_data['price'],
            quantity=product_data['quantity'],
            image=product_data.get('image')
        )
        
        product = Product(
            name=new_product.name,
            price=new_product.price,
            quantity=new_product.quantity,
            image=new_product.image,
            status=new_product.status,
            seller_id=seller_id
        )
        db.session.add(product)
        db.session.commit()
        
        return product
    
    @staticmethod
    def list_products(seller_id):
        products = Product.query.filter_by(seller_id=seller_id, status=True).all()
        product_list = []
        for product in products:
            product_list.append(product.to_dict())
        return product_list 
    
    @staticmethod
    def get_product(id, seller_id):
        product = Product.query.get(id)
        if not product or product.seller_id != seller_id:
            return None
        return product.to_dict()

    @staticmethod
    def update_product(id, data, seller_id):
        product = Product.query.get(id)
        if not product or product.seller_id != seller_id:
            return None
        for chave, valor in data.items():
            # optionally: validate keys before set
            setattr(product, chave, valor)
        db.session.commit()
        return product.to_dict()
    
    # @staticmethod
    # def sell_product(id, quantity, seller_id):

    
    @staticmethod
    def inactivate_product(id, seller_id):
        product = Product.query.get(id)
        if not product or product.seller_id != seller_id:
            return None
        product.status = False
        db.session.commit()
        return product.to_dict()