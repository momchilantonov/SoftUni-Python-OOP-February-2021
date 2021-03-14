from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self):

    @abstractmethod
    def sensors_count(self):
        pass


class Android(Robot):
    def __init__(self):
        super().__init__()

    def sensors_count(self):
        return 4


class Chappie(Robot):
    def __init__(self):
        super().__init__()

    def sensors_count(self):
        return 6

