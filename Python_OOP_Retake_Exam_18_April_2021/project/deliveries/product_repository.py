from project.deliveries.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        if product in self.products:
            raise ValueError(f"Product {product.name} already exists.")
        self.products.append(product)
        return f"Product {product.name} successfully added to inventory."

    @staticmethod
    def decrease(product: Product, quantity: int):
        product.quantity -= quantity
        return f"Left quantity of {product.name}: {product.quantity}"

    def find(self, product_name: str):
        try:
            product = [p for p in self.products if p.name == product_name][0]
        except IndexError:
            product = None
        if product is None:
            return "None"
        return product
