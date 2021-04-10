from abc import ABC, abstractmethod

from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        if not self.fish:
            names = 'none'
        else:
            names = " ".join([fish.name for fish in self.fish])
        return f"{self.name}:\n" \
               f'Fish: {names}\n' \
               f'Decorations: {len(self.decorations)}\n' \
               f'Comfort: {self.calculate_comfort()}\n'

    # def __str__(self):
    #     return f"{self.name}:\n" \
    #            f"Fish: {' '.join((fish.name for fish in self.fish) if self.fish else 'none')}\n" \
    #            f"Decorations: {len(self.decorations)}\n" \
    #            f"Comfort: {self.calculate_comfort()}"
