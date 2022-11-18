from products.product import Product
from products.shirt import Shirt
from products.shoes import Shoes
from products.suit_jacket import SuitJacket
from products.trousers import Trousers

from unittest import TestCase, main


class TestClothingStore(TestCase):
    def test_price(self):
        shirt91 = Shirt("Blue Cotton Shirt", "BrandS", 14.99, 'M', "blue")

        new_price = -15
        expected = 'Price must be a positive number!'

        with self.assertRaises(ValueError) as context:
            shirt91.price = new_price

        self.assertEqual(expected, str(context.exception))


    def test_shirt_size(self):
        shirt91 = Shirt("Blue Cotton Shirt", "BrandS", 14.99, 'M', "blue")

        new_size = '2XX'
        expected = 'Size must be one of these: XS, S, M, L, XL or 2XL!'

        with self.assertRaises(ValueError) as context:
            shirt91.size = new_size

        self.assertEqual(expected, str(context.exception))


    def test_shoes_size(self):
        shoes91 = Shoes('Black Leather Shoes', 'BrandS', 59.99, 43, 'black')

        new_size = 49
        expected = 'Size must be an even number between 39-46!'

        with self.assertRaises(ValueError) as context:
            shoes91.size = new_size

        self.assertEqual(expected, str(context.exception))


    def test_suit_jacket_sizes(self):
        jacket91 = SuitJacket('Black Cotton Suit Jacket', 'BrandJ', 99.99, 50, 'black')

        new_size = 47
        expected = 'Size must be an even number between 42-66!'

        with self.assertRaises(ValueError) as context:
            jacket91.size = new_size

        self.assertEqual(expected, str(context.exception))

    def test_trousers_sizes(self):
        trousers91 = Trousers('Black Cotton Trousers', 'BrandT', 29.99, 50, 'black')

        new_size = 49
        expected = 'Size must be an even number between 42-66!'

        with self.assertRaises(ValueError) as context:
            trousers91.size = new_size

        self.assertEqual(expected, str(context.exception))


if __name__ == '__main__':
    main()
