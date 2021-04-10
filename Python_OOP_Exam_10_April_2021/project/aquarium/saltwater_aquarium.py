from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    capacity = 25
    water = "Salty"

    def __init__(self, name):
        super().__init__(name, self.capacity)
