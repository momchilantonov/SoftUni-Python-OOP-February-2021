class Cheetah:
    MONEY_NEEDS = 60

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @staticmethod
    def get_needs():
        return Cheetah.MONEY_NEEDS
