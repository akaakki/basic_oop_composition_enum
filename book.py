from author import Author

class Book:
    
    def __init__(self, name: str, author: Author, price: float, qty= float):
        self.name = name
        self.author = author
        self.price = price
        self.qty = qty

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author
    
    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def set_qty(self, qty):
        self.qty = qty

    def get_qty(self):
        return self.qty

    def __str__(self):
        return f"Book[name={self.name}, {self.author},price={self.price},qty={self.qty}]"