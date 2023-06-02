class Product:
    def __init__(self, name, price, quantity):
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity

    # def __repr__(self) -> str:
    #     return f'{self.product_name} {self.product_price} {self.product_quantity}'


class Store:
    def __init__(self) -> None:
        self.__products_price = {}
        self.__products_quantity = {}
        self.__profit = 0

    def add_product(self, name, price, quantity):

        product = Product(name, price, quantity)

        self.__products_price[product.product_name] = product.product_price
        self.__products_quantity[product.product_name] = product.product_quantity

    def buy_product(self, name, quantity):
        if name in self.__products_price:
            if self.__products_quantity[name] >= quantity:

                # profit calculate
                self.__profit += ((5 *
                                  self.__products_price[name])/100) * quantity
                # deduct product quantity
                self.__products_quantity[name] -= quantity
                print("Thank you for purchasing")
            else:
                print("Unavailable")
        else:
            print("Not Found")

    def show_products(self):
        print("all products price: ", self.__products_price)
        print("all products quantity: ", self.__products_quantity)

    def show_profit(self):
        print("profit: ", self.__profit)


class Shop(Store):
    def __init__(self, name):
        self.shop_name = name
        super().__init__()


shop1 = Shop('Muntasir Store')
shop1.add_product('iphone', 400, 12)
shop1.add_product('asus laptop', 56000, 20)

# shop1.show_products()

# shop1.buy_product('iphone', 2)

shop1.buy_product('iphone', 2)
shop1.show_profit()
