from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    size = 5
    increase_size = 3
    water = "Salty"

    def __init__(self, name, species, price):
        super().__init__(name, species, self.size, price)
