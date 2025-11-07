from src.config.data_base import db 
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    seller = db.relationship('User', backref=db.backref('products', lazy=True, cascade="all, delete"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "image": self.image,
            "status": self.status,
            "seller_id": self.seller_id
        }
