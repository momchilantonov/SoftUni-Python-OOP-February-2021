from caretaker import Caretaker
from cheetah import Cheetah
from keeper import Keeper
from lion import Lion
from tiger import Tiger
from vet import Vet

NEW_LINE = "\n"


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
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
    def workers_capacity(self):
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
        if len(self.workers) < self.workers_capacity:
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
        total_salary = sum([worker.salary for worker in self.workers])
        if total_salary <= self.budget:
            self.budget = total_salary
            return f"You payed your workers. They are happy. Budget left: {self.budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_tend = sum([animal.get_needs() for animal in self.animals])
        if total_tend <= self.budget:
            self.budget = total_tend
            return f"You tended all the animals. They are happy. Budget left: {self.budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.is_profit = True
        self.budget = amount

    def animals_status(self):
        lions = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Lion']
        tigers = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        cheetahs = [animal.__repr__() for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{NEW_LINE.join(lions)}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{NEW_LINE.join(tigers)}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{NEW_LINE.join(cheetahs)}"

    def workers_status(self):
        keepers = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Keeper']
        caretakers = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Caretaker']
        vets = [worker.__repr__() for worker in self.workers if worker.__class__.__name__ == 'Vet']
        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{NEW_LINE.join(keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{NEW_LINE.join(caretakers)}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{NEW_LINE.join(vets)}"


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4),
           Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68),
           Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280),
           Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())
