import unittest

from Testing.testing_lab.worker.worker import Worker


class WorkerTest(unittest.TestCase):
    # Test if the worker is initialized with correct name, salary and energy
    def test_workerInit_CorrectNameSalaryEnergyInitialization(self):
        name = "Peter"
        salary = 1000
        energy = 100
        worker = Worker(name, salary, energy)
        self.assertEqual(name, worker.name)
        self.assertEqual(salary, worker.salary)
        self.assertEqual(energy, worker.energy)

    # Test if the worker's energy is incremented after the rest method is called
    def test_workerRest_CorrectEnergyIncrementation(self):
        name = "Ivan"
        salary = 800
        energy = 80
        worker = Worker(name, salary, energy)
        worker.rest()
        self.assertEqual(energy+1, worker.energy)

    # Test if an error is raised if the worker tries to work with negative energy or equal to 0
    def test_workerWork_RaiseErrorWithNegativeEnergy(self):
        name = "Maria"
        salary = 1200
        energy = 0
        worker = Worker(name, salary, energy)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertIsNotNone(context.exception)

    # Test if the worker's money is increased by his salary correctly after the work method is called
    def test_workerWork_CorrectMoneyIncrementation(self):
        name = "Boris"
        salary = 1900
        energy = 60
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(salary, worker.money)
        worker.work()
        self.assertEqual(salary * 2, worker.money)

    # Test if the worker's energy is decreased after the work method is called
    def test_workerWork_CorrectEnergyDecrease(self):
        name = "Nadya"
        salary = 1500
        energy = 90
        worker = Worker(name, salary, energy)
        worker.work()
        self.assertEqual(energy-1, worker.energy)

    # Test if the get_info method returns the proper string with correct values
    def test_workerGetInfo_CorrectStringValue(self):
        name = "Desi"
        salary = 1300
        energy = 50
        worker = Worker(name, salary, energy)
        expected = f'{name} has saved 0 money.'
        actual = worker.get_info()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
