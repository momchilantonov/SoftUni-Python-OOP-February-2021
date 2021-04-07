from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, self.get_salmon_grams())

    @staticmethod
    def get_salmon_grams():
        return Salmon.GRAMS
