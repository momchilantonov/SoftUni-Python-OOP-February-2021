from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    @staticmethod
    def get_fish(fish_type, fish_name, fish_species, price):
        fish = None
        if fish_type == 'FreshwaterFish':
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == 'SaltwaterFish':
            fish = SaltwaterFish(fish_name, fish_species, price)
        return fish

    def get_aquarium(self, aquarium_name):
        try:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        except IndexError:
            aquarium = None
        return aquarium

    def add_aquarium(self, aquarium_type, aquarium_name):
        valid_aquariums = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_aquariums:
            return "Invalid aquarium type."
        if aquarium_type == valid_aquariums[0]:
            aquarium = FreshwaterAquarium(aquarium_name)
        else:
            aquarium = SaltwaterAquarium(aquarium_name)
        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        valid_decorations = ["Ornament", "Plant"]
        if decoration_type not in valid_decorations:
            return "Invalid decoration type."
        if decoration_type == valid_decorations[0]:
            decoration = Ornament()
        else:
            decoration = Plant()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        aquarium = self.get_aquarium(aquarium_name)
        if aquarium is not None and not decoration == "None":
            aquarium.add_decoration(decoration)
            if self.decorations_repository.remove(decoration):
                return f"Successfully added {decoration_type} to {aquarium_name}."
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        valid_fish = ["FreshwaterFish", "SaltwaterFish"]
        if fish_type not in valid_fish:
            return f"There isn't a fish of type {fish_type}."
        fish = self.get_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.get_aquarium(aquarium_name)
        if not aquarium.water == fish.water:
            return "Water not suitable."
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium = self.get_aquarium(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = self.get_aquarium(aquarium_name)
        fish_price = sum(fish.price for fish in aquarium.fish)
        decorations_price = sum(decoration.price for decoration in aquarium.decorations)
        total_price = fish_price+decorations_price
        return f"The value of Aquarium {aquarium_name} is {total_price:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += aquarium.__str__()
        return result
