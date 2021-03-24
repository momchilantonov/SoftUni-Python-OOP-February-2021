import unittest
from Testing.testing_exercise.vehicle.project.project.vehicle import Vehicle
# from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50.0, 100.0)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 50.0)
        self.assertEqual(self.vehicle.horse_power, 100.0)

    def test_drive_when_enough_fuel_subtract_needed_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 37.5)

    def test_drive_when_not_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(100.0)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_refuel_when_fill_less_than_capacity_add_fuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(50.0)
        self.assertEqual(self.vehicle.fuel, 50.0)

    def test_refuel_when_fill_more_than_capacity_raise_exception(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(51.0)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_str(self):
        expected = f"The vehicle has 100.0 horse power with 50.0 fuel left and 1.25 fuel consumption"
        actual = self.vehicle.__str__()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
