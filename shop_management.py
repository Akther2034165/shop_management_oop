class Product:
    def __init__(self, name, price, quantity):
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity

    # def __repr__(self) -> str:
    #     return f'{self.product_name} {self.product_price} {self.product_quantity}'


class Store:
    def __init__(self):
        self.__products_price = {}
        self.__products_quantity = {}

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)

        # appending price and quantity to the dictionary
        self.__products_price[product.product_name] = product.product_price
        self.__products_quantity[product.product_name] = product.product_quantity

    def show_products(self):
        print("all product price: ", self.__products_price)
        print("all product quantity: ", self.__products_quantity)


class Shop(Store):
    def __init__(self, name):
        self.shop_name = name
        super().__init__()


shop1 = Shop('Muntasir Store')
shop1.add_product('iphone', 120000, 10)
shop1.add_product('asus laptop', 56000, 20)

shop1.show_products()
