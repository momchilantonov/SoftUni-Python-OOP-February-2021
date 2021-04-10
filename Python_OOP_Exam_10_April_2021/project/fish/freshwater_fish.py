from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    size = 3
    increase_size = 3
    water = "Fresh"

    def __init__(self, name, species, price):
        super().__init__(name, species, self.size, price)
