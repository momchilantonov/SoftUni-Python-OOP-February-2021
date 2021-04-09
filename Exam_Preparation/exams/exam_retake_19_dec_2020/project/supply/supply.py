from abc import ABC, abstractmethod

from project.survivor import Survivor


class Supply(ABC):
    @abstractmethod
    def __init__(self, needs_increase: int):
        self.needs_increase = needs_increase

    @property
    def needs_increase(self):
        return self.__needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self.__needs_increase = value

    def apply(self, survivor: Survivor):
        survivor.needs += self.needs_increase
