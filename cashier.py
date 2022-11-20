from products.shirt import Shirt
from products.shoes import Shoes
from products.suit_jacket import SuitJacket
from products.trousers import Trousers


class Cashier:
    def __init__(self):
        pass

    def print_receipt(self, products, date):
        self.calculate_discount(products, date)
        self.discount_price(products)
        result = ''
        result += f'Date: {date[:19]}\n' \
                  f'---Products---'

        for product in products:
            result += '\n'
            result += f'\n{product.name} - {product.brand}\n' \
                      f'${product.price:.2f}\n' \
                      f'#discount {product.discount_percentage:.0f}%  -${product.discount_price:.2f}'
        subtotal = self.subtotal(products)
        discount = self.discount(products)
        result += f'\n-----------------------------------------------------------------------------------\n'
        result += f'SUBTOTAL: ${subtotal:.2f}\n'
        result += f'DISCOUNT: -${discount:.2f}\n'
        result += f'TOTAL: ${(subtotal - discount):.2f}\n'
        return result

    @staticmethod
    def calculate_discount(products, date):
        for product in products:
            product.discount = 0
            if len(products) >= 3:
                if product.__class__.__name__ == "Shoes" and "Tuesday" in date:
                    product.discount = 0.25
                else:
                    product.discount = 0.2
            elif "Tuesday" in date:
                if product.__class__.__name__ == "Shirt":
                    product.discount = 0.1
                elif product.__class__.__name__ == "Shoes":
                    product.discount = 0.25
        return products

    @staticmethod
    def discount_price(products):
        for product in products:
            product.discount_price = round((product.discount * product.price), 2)
            product.discount_percentage = product.discount * 100

    @staticmethod
    def subtotal(products):
        return sum([product.price for product in products])

    @staticmethod
    def discount(products):
        return sum([product.discount_price for product in products])


cashier = Cashier()

shirt11 = Shirt("Blue Cotton Shirt", "BrandS", 14.99, 'M', "blue")
shirt12 = Shirt('White Cotton Shirt', 'BrandS', 15.99, 'M', 'white')
trousers11 = Trousers('Black Cotton Trousers', 'BrandT', 29.99, 50, 'black')
shoes11 = Shoes('Black Leather Shoes', 'BrandS', 59.99, 43, 'black')
jacket11 = SuitJacket('Black Cotton Suit Jacket', 'BrandJ', 99.99, 50, 'black')

products1 = [shirt11, shirt12, trousers11, shoes11, jacket11]
date1 = '2022-02-02 12:34:56'
print(cashier.print_receipt(products1, date1))

shirt21 = Shirt('Black Silk Shirt', 'BrandS', 29.99, 'L', 'black')
shirt22 = Shirt('White Silk Shirt', 'BrandS', 29.99, 'L', 'white')

products2 = [shirt21, shirt22]
date2 = '2022-02-01 12:34:56(Tuesday)'
print(cashier.print_receipt(products2, date2))

trousers31 = Trousers('Red Linen Trousers', 'BrandT', 49.99, 56, 'red')
shoes31 = Shoes('Red Suede Shoes', 'BrandS', 59.99, 44, 'red')
shoes32 = Shoes('Black Suede Shoes', 'BrandS', 59.99, 44, 'black')
jacket31 = SuitJacket('Red Linen Suit Jacket', 'BrandJ', 99.99, 56, 'red')
shirt31 = Shirt('White Linen Shirt', 'BrandS', 29.99, 'L', 'white')

products3 = [trousers31, shoes31, shoes32, jacket31, shirt31]
date3 = '2022-02-01 12:34:56(Tuesday)'
print(cashier.print_receipt(products3, date3))
