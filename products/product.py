from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def __init__(self, name, brand, price, color):
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if type(value) == int:
            value = float(value)
        if not value > 0 or not type(value) == float:
            raise ValueError("Price must be a positive number!")
        self.__price = value