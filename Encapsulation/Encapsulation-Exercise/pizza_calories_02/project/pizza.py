from dough import Dough
from topping import Topping


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
        toppings_weight = sum([tw for tw in self.toppings.values()])
        return toppings_weight
        # return toppings_weight+self.dough.weight

