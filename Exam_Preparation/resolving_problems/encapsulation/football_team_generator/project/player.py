class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        return f"Player: {self.name}\n" \
               f"Endurance: {self.endurance}\n" \
               f"Sprint: {self.sprint}\n" \
               f"Dribble: {self.dribble}\n" \
               f"Passing: {self.passing}\n" \
               f"Shooting: {self.shooting}\n"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        pass

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        pass

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        pass

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        pass

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        pass

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        pass
