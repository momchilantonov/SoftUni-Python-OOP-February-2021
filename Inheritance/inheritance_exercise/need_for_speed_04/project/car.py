from Inheritance.inheritance_exercise.need_for_speed_04.project.vehicle import Vehicle
# from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
