from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.animals_05.project.cat import Cat
# from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age, gender="Male"):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return "Hiss"

    def __repr__(self):
        return f"This is {self.name}. {self.name} " \
               f"is a {self.age} year old {self.gender} " \
               f"{self.__class__.__name__}"
