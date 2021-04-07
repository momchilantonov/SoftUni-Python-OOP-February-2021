from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name):
        super().__init__(name, self.get_cake_price(), self.get_cake_grams(), self.get_cake_calories())

    @staticmethod
    def get_cake_calories():
        cake_calories = Cake.CALORIES
        return cake_calories

    @staticmethod
    def get_cake_grams():
        cake_grams = Cake.GRAMS
        return cake_grams

    @staticmethod
    def get_cake_price():
        cake_price = Cake.PRICE
        return cake_price
