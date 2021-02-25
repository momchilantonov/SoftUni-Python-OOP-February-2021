from customer import Customer
from equipment import Equipment
from exercise_plan import ExercisePlan
from subscription import Subscription
from trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def is_customer(self, customer):
        return customer in self.customers

    def is_trainer(self, trainer):
        return trainer in self.trainers

    def is_equipment(self, equipment):
        return equipment in self.equipment

    def is_plan(self, plan):
        return plan in self.plans

    def is_subscription(self, subscription):
        return subscription in self.subscriptions

    def add_customer(self, customer):
        if not self.is_customer(customer):
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if not self.is_trainer(trainer):
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if not self.is_equipment(equipment):
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if not self.is_plan(plan):
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if not self.is_subscription(subscription):
            self.subscriptions.append(subscription)

    def find_subscription(self, id):
        return [s for s in self.subscriptions if id == s.id][0]

    def find_customer(self, id):
        return [c for c in self.customers if id == c.id][0]

    def find_trainer(self, id):
        return [t for t in self.trainers if id == t.id][0]

    def find_equipment(self, id):
        return [e for e in self.equipment if id == e.id][0]

    def find_plan(self, id):
        return [p for p in self.plans if id == p.id][0]

    def subscription_info(self, subscription_id):
        subscription_data = self.find_subscription(subscription_id)
        customer_data = self.find_customer(subscription_id)
        trainer_data = self.find_trainer(subscription_id)
        equipment_data = self.find_equipment(subscription_id)
        plan_data = self.find_plan(subscription_id)
        return f"{subscription_data}\n" \
               f"{customer_data}\n" \
               f"{trainer_data}\n" \
               f"{equipment_data}\n" \
               f"{plan_data}"


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))
