import unittest

from project.survivor import Survivor


class TestsSurvivor(unittest.TestCase):
    def setUp(self):
        self.survivor = Survivor("Pesho", 15)

    def test_init(self):
        self.assertEqual(self.survivor.name, "Pesho")
        self.assertEqual(self.survivor.age, 15)
        self.assertEqual(self.survivor.health, 100)
        self.assertEqual(self.survivor.needs, 100)

    def test_not_valid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.name = ""
        expected = str(ex.exception)
        actual = "Name not valid!"
        self.assertEqual(expected, actual)

    def test_not_valid_age(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.age = -1
        expected = str(ex.exception)
        actual = "Age not valid!"
        self.assertEqual(expected, actual)

    def test_not_valid_health(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.health = -1
        expected = str(ex.exception)
        actual = "Health not valid!"
        self.assertEqual(expected, actual)

    def test_not_valid_needs(self):
        with self.assertRaises(ValueError) as ex:
            self.survivor.needs = -1
        expected = str(ex.exception)
        actual = "Needs not valid!"
        self.assertEqual(expected, actual)

    def test_max_needs_false(self):
        self.assertEqual(self.survivor.needs_sustenance, False)

    def test_max_health_false(self):
        self.assertEqual(self.survivor.needs_healing, False)

    def test_max_needs(self):
        self.survivor.needs = 90
        self.assertEqual(self.survivor.needs_sustenance, True)

    def test_max_health(self):
        self.survivor.health = 90
        self.assertEqual(self.survivor.needs_healing, True)