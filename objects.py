class Product:
    def __init__(self, name: str, price: float, discount_percent: int):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def get_discount_amount(self):
        discount_amount = round(self.price * self.discount_percent / 100, 2)
        return discount_amount

    def get_discount_price(self):
        discount_price = round(self.price - self.get_discount_amount(), 2)
        return discount_price


def main():
    product1 = Product('Stanley 13 Ounce Wood Hammer', 12.99, 62)
    product2 = Product('National Hardware 3/4" Wire Nails', 5.06, 0)
    print(product1.get_discount_price())


if __name__ == "__main__":
    main()
