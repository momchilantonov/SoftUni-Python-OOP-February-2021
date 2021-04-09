from project.supply.supply import Supply


class FoodSupply(Supply):
    NEEDS_INCREASE = 20

    def __init__(self):
        super().__init__(self.get_needs_increase())

    @staticmethod
    def get_needs_increase():
        return FoodSupply.NEEDS_INCREASE
