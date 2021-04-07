from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    FUEL_CONSUMPTION_COEFFICIENT = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + Car.FUEL_CONSUMPTION_COEFFICIENT) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    FUEL_CONSUMPTION_COEFFICIENT = 1.6
    REFUEL_COEFFICIENT = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption+Truck.FUEL_CONSUMPTION_COEFFICIENT) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.REFUEL_COEFFICIENT


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
