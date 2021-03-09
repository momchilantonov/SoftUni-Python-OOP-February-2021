from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.wild_farm_04.project.animals.animal import \
    Mammal
from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.wild_farm_04.project.food import \
    Fruit, Meat, Vegetable


# from project.animals.animal import Mammal
# from project.food import Fruit, Meat, Vegetable


class Mouse(Mammal):
    WEIGHT_COEFFICIENT = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, (Fruit, Vegetable)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Mouse.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_COEFFICIENT = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Dog.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_COEFFICIENT = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        if not isinstance(food, (Meat, Vegetable)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Cat.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_COEFFICIENT = 1.00

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Tiger.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity
