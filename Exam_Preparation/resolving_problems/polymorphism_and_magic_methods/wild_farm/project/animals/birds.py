from project.animals.animal import Bird
from project.food import Food, Meat


class Owl(Bird):
    WEIGHT_INCREASE = 0.25
    FOOD = Meat

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Owl.FOOD):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += Owl.WEIGHT_INCREASE * food.quantity


class Hen(Bird):
    WEIGHT_INCREASE = 0.35
    FOOD = Food

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if not isinstance(food, Hen.FOOD):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += Hen.WEIGHT_INCREASE * food.quantity
