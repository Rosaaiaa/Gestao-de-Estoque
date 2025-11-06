class ProductDomain:
    def __init__(self, name, price, quantity, image):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.image = image
        self.status = True
    
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "image": self.image,
            "status": self.status
        }
