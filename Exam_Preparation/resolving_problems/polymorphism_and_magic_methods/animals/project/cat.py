from project.animal import Animal


class Cat(Animal):
    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    @staticmethod
    def make_sound():
        return "Meow meow!"

