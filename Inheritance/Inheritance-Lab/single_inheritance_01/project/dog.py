from animal import Animal


class Dog(Animal):
    @staticmethod
    def bark():
        return "barking..."


dog = Dog()
print(dog.eat())
print(dog.bark())

# test animal
# import unittest
#
#
# class Tests(unittest.TestCase):
#     def test_animal(self):
#         a = Animal()
#         res = a.eat()
#         self.assertEqual(res, "eating...")
#
#     def test_dog(self):
#         d = Dog()
#         res = d.bark()
#         self.assertEqual(res, "barking...")
#         self.assertEqual(d.__class__.__bases__[0].__name__, "Animal")
#
#
# if __name__ == "__main__":
#     unittest.main()
