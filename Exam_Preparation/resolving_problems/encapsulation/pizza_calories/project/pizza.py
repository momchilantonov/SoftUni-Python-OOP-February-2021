from project.topping import Topping
from project.dough import Dough


class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = toppings_capacity
        self.__toppings = {}
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__toppings_capacity = value

    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        pass

    def add_topping(self, topping):
        if topping.topping_type not in self.toppings:
            if self.toppings_capacity >= topping.weight:
                self.toppings[topping.topping_type] = topping.weight
            else:
                raise ValueError("Not enough space for another topping")
        else:
            self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self):
        total_toppings_weight = sum(t for t in self.toppings.values())
        dough_weight = self.dough.weight
        pizza_weight = total_toppings_weight+dough_weight
        return pizza_weight


# import unittest
#
# # from project.dough import Dough
# # from project.pizza import Pizza
# # from project.topping import Topping
#
#
# class Tests(unittest.TestCase):
#     def test_topping_init(self):
#         t = Topping("Tomato", 20)
#         self.assertEqual(t._Topping__topping_type, "Tomato")
#         self.assertEqual(t._Topping__weight, 20)
#
#     def test_dough_init(self):
#         d = Dough("Sugar", "Mixing", 20)
#         self.assertEqual(d._Dough__flour_type, "Sugar")
#         self.assertEqual(d._Dough__baking_technique, "Mixing")
#         self.assertEqual(d._Dough__weight, 20)
#
#     def test_pizza_init(self):
#         d = Dough("Sugar", "Mixing", 20)
#         p = Pizza("Burger", d, 5)
#
#         self.assertEqual(p._Pizza__name, "Burger")
#         self.assertEqual(p._Pizza__dough, d)
#         self.assertEqual(len(p._Pizza__toppings), 0)
#         self.assertEqual(p._Pizza__toppings_capacity, 5)
#
#     def test_pizza_add_topping_error(self):
#         d = Dough("Sugar", "Mixing", 20)
#         t = Topping("Tomato", 20)
#         p = Pizza("Burger", d, 0)
#         with self.assertRaises(ValueError) as ctx:
#             p.add_topping(t)
#         self.assertEqual("Not enough space for another topping", str(ctx.exception))
#
#     def test_pizza_add_topping_new(self):
#         d = Dough("Sugar", "Mixing", 20)
#         t = Topping("Tomato", 20)
#         p = Pizza("Burger", d, 200)
#         p.add_topping(t)
#
#         self.assertEqual(p.toppings["Tomato"], 20)
#         self.assertEqual(len(p.toppings), 1)
#
#     def test_pizza_add_topping_update(self):
#         d = Dough("Sugar", "Mixing", 20)
#         t = Topping("Tomato", 20)
#         p = Pizza("Burger", d, 200)
#         p.add_topping(t)
#         p.add_topping(t)
#
#         self.assertEqual(p.toppings["Tomato"], 40)
#
#     def test_pizza_calculate_total_weight(self):
#         d = Dough("Sugar", "Mixing", 20)
#         t = Topping("Tomato", 20)
#         p = Pizza("Burger", d, 200)
#         p.add_topping(t)
#         p.add_topping(t)
#
#         self.assertEqual(p.calculate_total_weight(), 60)
#
#
# if __name__ == '__main__':
#     unittest.main()
