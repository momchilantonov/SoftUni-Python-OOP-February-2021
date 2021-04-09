from project.software.software import Software


class LightSoftware(Software):
    TYPE = "Light"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, LightSoftware.TYPE, int(capacity_consumption * 1.5), int(memory_consumption * 0.5))
