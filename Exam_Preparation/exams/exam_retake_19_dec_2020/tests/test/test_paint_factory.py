import unittest

# from tests.project.factory.paint_factory import PaintFactory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("PF", 100)

    def test__init(self):
        self.assertEqual(self.paint_factory.name, "PF")
        self.assertEqual(self.paint_factory.capacity, 100)
        self.assertEqual(self.paint_factory.ingredients, {})
        self.assertEqual(self.paint_factory.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test__prop_products__return_ingredients_dict(self):
        self.assertEqual(self.paint_factory.products, {})

    def test__add_ingredient__non_type__raise_type_error(self):
        with self.assertRaises(TypeError) as te:
            self.paint_factory.add_ingredient("magenta", 100)
        expected_msg = str(te.exception)
        actual_msg = "Ingredient of type magenta not allowed in PaintFactory"
        self.assertEqual(expected_msg, actual_msg)

    def test__add_ingredient___less_capacity__raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.paint_factory.add_ingredient("blue", 110)
            expected_msg = str(ve.exception)
            actual_msg = "Not enough space in factory"
            self.assertEqual(expected_msg, actual_msg)

    def test_inherits_from_factory(self):
        self.assertTrue(issubclass(PaintFactory, Factory))

    def test__add_ingredient__add_in_dict__set_val_to_qty(self):
        self.assertEqual(self.paint_factory.products, {})
        self.paint_factory.add_ingredient("blue", 10)
        self.assertEqual(self.paint_factory.products, {"blue": 10})
        self.paint_factory.add_ingredient("red", 10)
        self.assertEqual(self.paint_factory.products, {"blue": 10, "red": 10})
        self.paint_factory.add_ingredient("red", 10)
        self.assertEqual(self.paint_factory.products, {"blue": 10, "red": 20})

    def test__remove_ingredient__not_in_dict__raise_key_error(self):
        self.paint_factory.add_ingredient("blue", 100)
        with self.assertRaises(KeyError) as ke:
            self.paint_factory.remove_ingredient("magenta", 10)
        expected_msg = str(ke.exception)
        actual_msg = "'No such product in the factory'"
        self.assertEqual(expected_msg, actual_msg)

    def test__remove_ingredient__more_qty__raise_value_error(self):
        self.paint_factory.add_ingredient("blue", 100)
        with self.assertRaises(ValueError) as ve:
            self.paint_factory.remove_ingredient("blue", 110)
        expected_msg = str(ve.exception)
        actual_msg = "Ingredient quantity cannot be less than zero"
        self.assertEqual(expected_msg, actual_msg)

    def test_remove_ingredient_quantity(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.remove_ingredient("white", 3)
        self.assertEqual(self.paint_factory.ingredients, {"white": 2})
        self.paint_factory.remove_ingredient("white", 2)
        self.assertEqual(self.paint_factory.ingredients, {"white": 0})

    def test__remove_ingredient__remove_qty_from_ingredient_val(self):
        self.paint_factory.add_ingredient("blue", 100)
        self.paint_factory.remove_ingredient("blue", 50)
        self.assertEqual(self.paint_factory.products, {"blue": 50})

    def test_get_ingredients(self):
        self.paint_factory.add_ingredient("white", 5)
        self.paint_factory.add_ingredient("yellow", 10)
        dict = self.paint_factory.ingredients
        self.assertEqual(dict, {"white": 5, "yellow": 10})

    def test__can_add__return_true(self):
        self.assertTrue(self.paint_factory.can_add(10))
        self.assertFalse(self.paint_factory.can_add(110))

    def test_add_zero(self):
        self.paint_factory.add_ingredient("white", 0)
        self.assertEqual(self.paint_factory.products, {"white": 0})

    def test_can_add(self):
        self.paint_factory.add_ingredient("white", 5)
        self.assertEqual(self.paint_factory.can_add(100), False)
        self.assertEqual(self.paint_factory.can_add(10), True)

    def test_if_isinstance(self):
        self.assertIsInstance(PaintFactory, Factory)


if __name__ == "__main__":
    unittest.main()
