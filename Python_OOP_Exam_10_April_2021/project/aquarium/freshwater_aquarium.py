from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    capacity = 50
    water = "Fresh"

    def __init__(self, name):
        super().__init__(name, self.capacity)
