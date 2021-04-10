import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self):
        self.train = Train("Train", 2)

    def test__init(self):
        self.assertEqual(self.train.name, "Train")
        self.assertEqual(self.train.capacity, 2)
        self.assertEqual(self.train.passengers, [])

    def test__add__no_cap__raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.train.add("Pesho")
            self.train.add("Gosho")
            self.train.add("Maria")
        expected_msg = str(ex.exception)
        actual_msg = "Train is full"
        self.assertEqual(expected_msg, actual_msg)

    def test__add__same_name__raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.train.add("Pesho")
            self.train.add("Pesho")
        expected_msg = str(ex.exception)
        actual_msg = "Passenger Pesho Exists"
        self.assertEqual(expected_msg, actual_msg)

    def test__add__add_passenger(self):
        self.train.add("Pesho")
        self.assertEqual(len(self.train.passengers), 1)
        self.assertEqual(self.train.add("Maria"), "Added passenger Maria")
        self.assertEqual(len(self.train.passengers), 2)

    def test__remove_not_passenger_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Pesho")
        expected_msg = str(ex.exception)
        actual_msg = "Passenger Not Found"
        self.assertEqual(expected_msg, actual_msg)

    def test__remove__remove_passenger(self):
        self.train.add("Pesho")
        self.assertEqual(len(self.train.passengers), 1)
        self.train.remove("Pesho")
        self.assertEqual(len(self.train.passengers), 0)
        self.train.add("Pesho")
        self.assertEqual(self.train.remove("Pesho"), "Removed Pesho")


if __name__ == "__main__":
    unittest.main()
