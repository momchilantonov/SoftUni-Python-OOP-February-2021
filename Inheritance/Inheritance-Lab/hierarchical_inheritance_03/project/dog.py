from animal import Animal


class Dog(Animal):

    @staticmethod
    def bark():
        return "barking..."


dog = Dog()
print(dog.eat())
print(dog.bark())