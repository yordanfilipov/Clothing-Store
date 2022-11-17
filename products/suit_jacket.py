from products.product import Product


class SuitJacket(Product):
    sizes = [42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66]

    def __init__(self, name, brand, price, size, color):
        super().__init__(name, brand, price, color)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value not in SuitJacket.sizes:
            raise ValueError("Size must be an even number between 42-66!")
        self.__size = value
