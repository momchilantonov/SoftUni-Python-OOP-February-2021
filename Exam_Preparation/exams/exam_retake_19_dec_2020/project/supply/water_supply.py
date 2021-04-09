from project.supply.supply import Supply


class WaterSupply(Supply):
    NEEDS_INCREASE = 40

    def __init__(self):
        super().__init__(self.get_needs_increase())

    @staticmethod
    def get_needs_increase():
        return WaterSupply.NEEDS_INCREASE
