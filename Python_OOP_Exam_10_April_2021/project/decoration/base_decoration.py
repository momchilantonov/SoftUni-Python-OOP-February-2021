from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price
