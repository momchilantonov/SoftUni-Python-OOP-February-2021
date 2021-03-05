from Inheritance.inheritance_exercise.need_for_speed_04.project.car import Car
# from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = SportCar.DEFAULT_FUEL_CONSUMPTION
