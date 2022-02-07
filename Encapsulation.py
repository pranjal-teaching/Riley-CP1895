from dataclasses import dataclass


@dataclass
class Product:
    __price: float = 0.0
    name: str = ""
    discount_percent: int = 0

    def __post_init__(self):
        self.price = self.__price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        assert price >= 0, ValueError
        self.__price = price

    def get_discount_amount(self):
        discount_amount = round(self.__price * self.discount_percent / 100, 2)
        return discount_amount

    def get_discount_price(self):
        discount_price = round(self.__price - self.get_discount_amount(), 2)
        return discount_price


def main():
    product_test = Product(1, "Test", 7)
    product_test.price = 100


if __name__ == "__main__":
    main()
