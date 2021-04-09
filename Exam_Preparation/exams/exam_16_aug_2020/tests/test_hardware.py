import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("H", "Heavy", 100, 100)
        self.software = ExpressSoftware("S", 10, 10)

    def test__init(self):
        self.assertEqual(self.hardware.name, "H")
        self.assertEqual(self.hardware.type, "Heavy")
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.memory, 100)
        self.assertEqual(self.hardware.software_components, [])

    def test__prop_available_memory__return_result(self):
        self.hardware.install(self.software)
        self.assertEqual(self.hardware.available_memory, 80)

    def test__prop_available_capacity__return_result(self):
        self.hardware.install(self.software)
        self.assertEqual(self.hardware.available_capacity, 90)

    def test__install_software_without_enough_capacity__raise_exception(self):
        self.hardware.capacity = 100
        self.software.capacity_consumption = 110
        with self.assertRaises(Exception) as exception:
            self.hardware.install(self.software)
        expected_msg = str(exception.exception)
        actual_msg = "Software cannot be installed"
        self.assertEqual(actual_msg, expected_msg)

    def test__install_software_without_enough_memory__raise_exception(self):
        self.hardware.memory = 100
        self.software.memory_consumption = 110
        with self.assertRaises(Exception) as exception:
            self.hardware.install(self.software)
        expected_msg = str(exception.exception)
        actual_msg = "Software cannot be installed"
        self.assertEqual(actual_msg, expected_msg)

    def test__install_software_with_enough_capacity_and_memory__add_software_in_software_components(self):
        self.hardware.install(self.software)
        self.assertIn(self.software, self.hardware.software_components)

    def test__uninstall_software__remove_software_from_software_components(self):
        self.hardware.install(self.software)
        self.assertIn(self.software, self.hardware.software_components)
        self.hardware.uninstall(self.software)
        self.assertNotIn(self.software, self.hardware.software_components)


if __name__ == "__main__":
    unittest.main()
