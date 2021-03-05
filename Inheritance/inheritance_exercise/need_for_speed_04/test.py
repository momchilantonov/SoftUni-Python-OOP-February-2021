from Inheritance.inheritance_exercise.need_for_speed_04.project.vehicle import Vehicle
from Inheritance.inheritance_exercise.need_for_speed_04.project.race_motorcycle import RaceMotorcycle
from Inheritance.inheritance_exercise.need_for_speed_04.project.family_car import FamilyCar


vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)

print("------------")

m = RaceMotorcycle(200, 100)
print(m.DEFAULT_FUEL_CONSUMPTION)
print(m.fuel)
print(m.horse_power)
print(m.fuel_consumption)
m.drive(10)
print(m.fuel)