from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.name = name
        self.animals = []
        self.workers = []
        self.is_profit = False

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if self.is_profit:
            self.__budget += value
            self.is_profit = False
        else:
            self.__budget -= value

    @property
    def animal_capacity(self):
        return self.__animal_capacity

    @property
    def worker_capacity(self):
        return self.__workers_capacity

    def add_animal(self, animal, price):
        if len(self.animals) < self.animal_capacity:
            if price <= self.budget:
                self.animals.append(animal)
                self.budget = price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.worker_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(worker.salary for worker in self.workers)
        if total_salaries <= self.budget:
            self.budget = total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_money_needs = sum(animal.get_needs() for animal in self.animals)
        if total_money_needs <= self.budget:
            self.budget = total_money_needs
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.is_profit = True
        self.budget = amount

    def animals_status(self):
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]
        result = f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"
        for lion in lions:
            result += lion.__repr__()+"\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += tiger.__repr__()+"\n"
        result += f"----- {len(tigers)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += cheetah.__repr__()+"\n"
        return result.strip()

    def workers_status(self):
        keepers = [worker for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [worker for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [worker for worker in self.workers if isinstance(worker, Vet)]
        result = f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += keeper.__repr__()+"\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += caretaker.__repr__()+"\n"
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += vet.__repr__()+"\n"
        return result.strip()


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
#            Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
#            Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
#            Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
