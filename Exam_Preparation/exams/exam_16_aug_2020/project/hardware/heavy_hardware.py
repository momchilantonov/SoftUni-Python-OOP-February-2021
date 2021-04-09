from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    TYPE = "Heavy"

    def __init__(self, name, capacity, memory):
        super().__init__(name, HeavyHardware.TYPE, capacity * 2, int(memory * 0.75))
