import unittest
from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.card = MagicCard("Wow")

    def test__init(self):
        self.assertEqual(self.card.name, "Wow")
        self.assertEqual(self.card.damage_points, 5)
        self.assertEqual(self.card.health_points, 80)

    def test__set_name_with_empty_string__raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.card.name = ""
        expected_msg = str(context.exception)
        actual_msg = "Card's name cannot be an empty string."
        self.assertEqual(expected_msg, actual_msg)

    def test__set_damage_point_below_zero__raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.card.damage_points = -1
        expected_msg = str(context.exception)
        actual_msg = "Card's damage points cannot be less than zero."
        self.assertEqual(expected_msg, actual_msg)

    def test__set_health_points_below_zero__raise_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.card.health_points = -1
        expected_msg = str(context.exception)
        actual_msg = "Card's HP cannot be less than zero."
        self.assertEqual(expected_msg, actual_msg)


if __name__ == "__main__":
    unittest.main()
