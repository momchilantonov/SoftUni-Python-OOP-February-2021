from project.medicine.medicine import Medicine


class Painkiller(Medicine):
    HEALTH_INCREASE = 20

    def __init__(self):
        super().__init__(self.get_health_increase())

    @staticmethod
    def get_health_increase():
        return Painkiller.HEALTH_INCREASE
