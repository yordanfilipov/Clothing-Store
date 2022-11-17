from products.product import Product


class Shoes(Product):
    sizes = [39, 40, 41, 42, 43, 44, 45, 46]

    def __init__(self, name, brand, price, size, color):
        super().__init__(name, brand, price, color)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value not in Shoes.sizes:
            raise ValueError("Size must be an even number between 39-46!")
        self.__size = value
