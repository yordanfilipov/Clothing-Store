from products.product import Product


class Shirt(Product):
    sizes = ['XS', 'S', 'M', 'L', 'XL', '2XL']

    def __init__(self, name, brand, price, size, color):
        super().__init__(name, brand, price, color)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value not in Shirt.sizes:
            raise ValueError("Size must be one of these: XS, S, M, L, XL or 2XL!")
        self.__size = value

