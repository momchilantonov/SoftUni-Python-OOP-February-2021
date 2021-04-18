from project.deliveries.product import Product


class Food(Product):
    quantity = 15

    def __init__(self, name):
        super().__init__(name, self.quantity)
