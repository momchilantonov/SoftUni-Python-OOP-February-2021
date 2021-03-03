class Tiger:
    tend_needs = 45

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs():
        return Tiger.tend_needs

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"