from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.wild_farm_04.project.animals.animal import \
    Bird
from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.wild_farm_04.project.food import \
    Meat


# from project.animals.animal import Bird
# from project.food import Meat


class Owl(Bird):
    WEIGHT_COEFFICIENT = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Owl.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_COEFFICIENT = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        self.weight += Hen.WEIGHT_COEFFICIENT * food.quantity
        self.food_eaten += food.quantity
