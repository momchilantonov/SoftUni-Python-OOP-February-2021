from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        total_memory = sum(h.memory for h in System._hardware)
        total_used_memory = sum(s.memory_consumption for s in System._software)
        total_capacity = sum(h.capacity for h in System._hardware)
        total_used_space = sum(s.capacity_consumption for s in System._software)

        return f"System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {total_used_memory} / {total_memory}\n" \
               f"Total Capacity Taken: {total_used_space} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            express_software = [s for s in h.software_components if s.type == "Express"]
            light_software = [s for s in h.software_components if s.type == "Light"]
            total_used_memory = sum(s.memory_consumption for s in h.software_components)
            total_used_space = sum(s.capacity_consumption for s in h.software_components)
            software_names = ', '.join(h.name for h in h.software_components)
            result += f"Hardware Component - {h.name}\n" \
                      f"Express Software Components: {len(express_software)}\n" \
                      f"Light Software Components: {len(light_software)}\n" \
                      f"Memory Usage: {total_used_memory} / {h.memory}\n" \
                      f"Capacity Usage: {total_used_space} / {h.capacity}\n" \
                      f"Type: {h.type}\n" \
                      f"Software Components: {software_names if software_names else 'None'}"
        return result
