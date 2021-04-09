class Survivor:
    MAX_HEALTH = 100
    MAX_NEEDS = 100

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.health: int = self.get_max_health()
        self.needs: int = self.get_max_needs()

    @staticmethod
    def get_max_health():
        return Survivor.MAX_HEALTH

    @staticmethod
    def get_max_needs():
        return Survivor.MAX_NEEDS

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self.__age = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        if value > self.get_max_health():
            self.__health = self.get_max_health()
        else:
            self.__health = value

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        if value > self.get_max_needs():
            self.__needs = self.get_max_needs()
        else:
            self.__needs = value

    @property
    def needs_sustenance(self):
        return self.needs < self.get_max_needs()

    @property
    def needs_healing(self):
        return self.health < self.get_max_health()
