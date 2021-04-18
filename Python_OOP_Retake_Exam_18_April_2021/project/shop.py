from project.deliveries.drink import Drink
from project.deliveries.food import Food
from project.deliveries.product_repository import ProductRepository
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository


class Shop:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    @staticmethod
    def __create_product(product_type, product_name):
        product = None
        if product_type == 'Drink':
            product = Drink(product_name)
        elif product_type == 'Food':
            product = Food(product_name)
        return product

    def deliver(self, product_type: str, name: str):
        product = self.__create_product(product_type, name)
        if product in self.product_repository.products:
            raise ValueError(f"Product {product.name} already exists.")
        return self.product_repository.add(product)

    def sell(self, customer_name: str, **shopping_list):
        customer = self.customer_repository.find(customer_name)
        if customer == "None":
            customer = Customer(customer_name)
            self.customer_repository.add(customer)
        result = ""
        for product_name, quantity in shopping_list.items():
            product = self.product_repository.find(product_name)
            if not product == "None":
                if quantity < product.quantity:
                    customer.products[product_name] = quantity
                    result += self.product_repository.decrease(product, quantity)
                else:
                    customer.products[product_name] = product.quantity
                    result += self.product_repository.decrease(product, product.quantity)
                    self.product_repository.products.remove(product)
        return result
