from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The product cannot be an empty string.")
        self.__name = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity cannot be equal to or below zero.")
        self.__quantity = value
