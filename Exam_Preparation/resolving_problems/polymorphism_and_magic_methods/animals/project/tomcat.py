from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    @staticmethod
    def make_sound():
        return "Hiss"
