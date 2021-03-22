import unittest

# from Testing.testing_lab.car_manager.car_manager import Car


class TestCar(unittest.TestCase):
    def __get_exception_from_init(self, make, model, fuel_consumption, fuel_capacity):
        with self.assertRaises(Exception) as context:
            Car(make, model, fuel_consumption, fuel_capacity)
        return context.exception

    def test_carInit_CorrectValuesInitialization(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        car = Car(make, model, fuel_consumption, fuel_capacity)
        expected = [make, model, fuel_consumption, fuel_capacity, 0]
        actual = [car.make, car.model, car.fuel_consumption, car.fuel_capacity, car.fuel_amount]
        self.assertListEqual(expected, actual)

    def test_carInit_WithNoneMake_RaiseException(self):
        make = None
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_WithEmptyStringMake_RaiseException(self):
        make = ""
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_WithNoneModel_RaiseException(self):
        make = "Test make"
        model = None
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_WithEmptyStringModel_RaiseException(self):
        make = "Test make"
        model = ""
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_WithNegativeFuelConsumption_RaiseException(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = -1
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_WithZeroFuelConsumption_RaiseException(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 0
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_WithNegativeFuelCapacity_RaiseException(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = -1
        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_WithZeroFuelCapacity_RaiseException(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 0
        params = [make, model, fuel_consumption, fuel_capacity]
        exception = self.__get_exception_from_init(*params)
        self.assertIsNotNone(exception)

    def test_carInit_WithNegativeFuelAmount_RaiseException(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as context:
            car.fuel_amount = -1
        self.assertIsNotNone(context.exception)

    def test_carRefuel_WithNegativeFuel_RaiseException(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as context:
            car.refuel(-1)
        self.assertIsNotNone(context.exception)

    def test_carRefuel_WithZeroFuel_RaiseException(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as context:
            car.refuel(0)
        self.assertIsNotNone(context.exception)

    def test_carRefuel_WithPositiveFuel_IncreaseAmount(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        car.refuel(5)
        self.assertEqual(5, car.fuel_amount)

    def test_carRefuel_WithMoreFuel_SetAmount(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        car.refuel(car.fuel_capacity * 2)
        self.assertEqual(car.fuel_capacity, car.fuel_amount)

    def test_carDrive_WithNotEnoughFuel_RaiseException(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        car.refuel(car.fuel_capacity)
        distance = 100
        car.drive(distance)
        expected = car.fuel_capacity - car.fuel_consumption * distance / 100
        actual = car.fuel_amount
        self.assertEqual(expected, actual)

    def test_carDrive_WithEnoughFuel_DecreaseAmount(self):
        make = "Test make"
        model = "Test model"
        fuel_consumption = 6
        fuel_capacity = 60
        params = [make, model, fuel_consumption, fuel_capacity]
        car = Car(*params)
        with self.assertRaises(Exception) as context:
            car.drive(100)
        self.assertIsNotNone(context.exception)


if __name__ == "__main__":
    unittest.main()
