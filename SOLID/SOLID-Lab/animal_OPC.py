from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.sound = "Meow"

    def make_sound(self):
        return self.sound


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.sound = "Woof-woof"

    def make_sound(self):
        return self.sound


animals = [Cat(), Dog()]
for animal in animals:
    print(animal.make_sound())
