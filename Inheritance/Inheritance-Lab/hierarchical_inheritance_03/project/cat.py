from animal import Animal


class Cat(Animal):

    @staticmethod
    def meow():
        return "meowing..."


cat = Cat()
print(cat.eat())
print(cat.meow())
