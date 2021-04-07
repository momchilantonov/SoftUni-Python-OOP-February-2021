# from project.product import Product
# from project.beverage.beverage import Beverage
from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name, caffeine):
        super().__init__(name, self.get_coffee_price(), self.get_coffee_milliliters())
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @staticmethod
    def get_coffee_price():
        return Coffee.PRICE

    @staticmethod
    def get_coffee_milliliters():
        return Coffee.MILLILITERS
