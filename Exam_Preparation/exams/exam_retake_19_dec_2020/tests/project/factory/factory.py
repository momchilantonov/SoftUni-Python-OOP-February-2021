# from abc import ABC, abstractmethod
#
#
# class Factory(ABC):
#     @abstractmethod
#     def __init__(self, name: str, capacity: int):
#         self.name = name
#         self.capacity = capacity
#         self.ingredients = {}  # key: name of the ingredient and value: quantity of the ingredient
#
#     @abstractmethod
#     def add_ingredient(self, ingredient_type: str, quantity: int):
#         pass
#
#     @abstractmethod
#     def remove_ingredient(self, ingredient_type: str, quantity: int):
#         pass
#
#     def can_add(self, value: int):
#         return self.capacity >= sum(self.ingredients.values()) + value

from project.factory.paint_factory import PaintFactory
from project.factory.factory import Factory
import unittest


class PaintFactoryTests(unittest.TestCase):

    def setUp(self):
        self.paint_factory = PaintFactory("name", 100)
        # self.valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def test_paint_factory_initialized(self):
        self.assertEqual(self.paint_factory.name, "name")
        self.assertEqual(self.paint_factory.capacity, 100)
        self.assertEqual(self.paint_factory.ingredients, {})
        self.assertEqual(self.paint_factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_add_ingredient_ingredient_type_not_in_list(self):
        self.assertRaises(TypeError, self.paint_factory.add_ingredient, "brown", 5)

    def test_add_ingredient_capacity_less_than_quantity(self):
        self.assertRaises(ValueError, self.paint_factory.add_ingredient, "green", 105)

    def test_inherits_from_factory(self):
        self.assertTrue(issubclass(PaintFactory, Factory))

    def test_add_zero(self):
        self.paint_factory.add_ingredient("white", 0)
        self.assertEqual(self.paint_factory.ingredients, {"white": 0})

    def test_add_ingredient_add_new_ingredient_type(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual(self.paint_factory.ingredients, {"white": 5})

    def test_remove_ingredient_ingredient_type_not_in_list(self):
        self.assertRaises(KeyError, self.paint_factory.remove_ingredient, "brown", 5)

    def test_remove_ingredient_quantity_more_than_existing(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertRaises(ValueError, self.paint_factory.remove_ingredient, "white", 6)

    def test_remove_ingredient_quantity(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.remove_ingredient("white", 3)
        self.assertEqual(self.paint_factory.ingredients, {"white": 2})
        self.paint_factory.remove_ingredient("white", 2)
        self.assertEqual(self.paint_factory.ingredients, {"white": 0})

    def test_get_ingredients(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.add_ingredient("yellow", 10)
        dict = self.paint_factory.ingredients
        self.assertEqual(dict, {"white": 5, "yellow": 10})

    def test_can_add(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual(self.paint_factory.can_add(100), False)
        self.assertEqual(self.paint_factory.can_add(10), True)

    def test_if_instanse(self):
        self.assertIsInstance(PaintFactory)

    def test_property_products(self):
        self.assertEqual({}, self.paint_factory.products)


if __name__ == "__main__":
    unittest.main()
