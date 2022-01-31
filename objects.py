class Product:
    def __init__(self, name: str, price: float, discount_percent: int):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def get_discount_amount(self):
        discount_amount = self.price * self.discount_percent / 100
        return discount_amount

    def get_discount_price(self):
        discount_price = self.price - self.get_discount_amount()
        return discount_price
