import unittest
from Testing.testing_exercise.mammal.project.project.mammal import Mammal
# from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self):
        name = "Leo"
        type = "Lion"
        sound = "Grrr..."
        self.mammal = Mammal(name, type, sound)

    def test_init(self):
        self.assertEqual(self.mammal.name, "Leo")
        self.assertEqual(self.mammal.type, "Lion")
        self.assertEqual(self.mammal.sound, "Grrr...")

    def test_make_sound(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        actual = self.mammal.make_sound()
        self.assertEqual(expected, actual)

    def test_privet_attribute(self):
        privet_attribute = self.mammal._Mammal__kingdom
        privet_result = "animals"
        self.assertEqual(privet_attribute, privet_result)

    def test_get_kingdom(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()
        self.assertEqual(expected, actual)

    def test_info(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
