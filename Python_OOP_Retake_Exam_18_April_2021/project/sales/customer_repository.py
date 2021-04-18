from project.sales.customer import Customer


class CustomerRepository:
    def __init__(self):
        self.customers = []

    def add(self, customer: Customer):
        if customer in self.customers:
            raise ValueError(f"Customer {customer.name} already exists.")
        self.customers.append(customer)

    def remove(self, customer_name: str):
        customer = self.find(customer_name)
        if customer == "None":
            raise ValueError(f"Customer {customer_name} does not exist.")
        self.customers.remove(customer)
        return f"Removed customer: {customer_name}"

    def find(self, customer_name: str):
        try:
            customer = [c for c in self.customers if c.name == customer_name][0]
        except IndexError:
            customer = None
        if customer is None:
            return "None"
        return customer
