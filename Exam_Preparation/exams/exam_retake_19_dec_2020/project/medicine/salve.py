from project.medicine.medicine import Medicine


class Salve(Medicine):
    HEALTH_INCREASE = 50

    def __init__(self):
        super().__init__(self.get_health_increase())

    @staticmethod
    def get_health_increase():
        return Salve.HEALTH_INCREASE
