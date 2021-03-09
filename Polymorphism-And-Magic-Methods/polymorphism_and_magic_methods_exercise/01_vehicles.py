from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    @staticmethod
    def can_drive(consumption, fuel):
        return consumption <= fuel


class Car(Vehicle):
    ADD_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + Car.ADD_CONSUMPTION)
        if self.can_drive(consumption, self.fuel_quantity):
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    ADD_CONSUMPTION = 1.6
    REFUEL_PROBLEM = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + Truck.ADD_CONSUMPTION)
        if self.can_drive(consumption, self.fuel_quantity):
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.REFUEL_PROBLEM


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

print("----------")

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
