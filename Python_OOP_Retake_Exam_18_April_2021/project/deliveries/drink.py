from project.deliveries.product import Product


class Drink(Product):
    quantity = 10

    def __init__(self, name):
        super().__init__(name, self.quantity)
