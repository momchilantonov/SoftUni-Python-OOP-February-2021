from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10
    FOOD = Vegetable, Fruit

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Mouse.FOOD):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += Mouse.WEIGHT_INCREASE * food.quantity


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40
    FOOD = Meat

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Dog.FOOD):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += Dog.WEIGHT_INCREASE * food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30
    FOOD = Vegetable, Meat

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Cat.FOOD):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += Cat.WEIGHT_INCREASE * food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00
    FOOD = Meat

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Tiger.FOOD):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += Tiger.WEIGHT_INCREASE * food.quantity
