from .factory import Factory


class PaintFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.valid_ingredients = ["white", "yellow", "blue", "green", "red"]

    def add_ingredient(self, ingredient_type: str, quantity: int):

        if ingredient_type not in self.valid_ingredients:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in PaintFactory")
        elif self.capacity < quantity:
            raise ValueError("Not enough space in factory")
        elif ingredient_type not in self.ingredients.keys():
            self.ingredients[ingredient_type] = 0

        self.ingredients[ingredient_type] += quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients.keys():
            raise KeyError("No such product in the factory")
        elif quantity > self.ingredients[ingredient_type]:
            raise ValueError("Ingredient quantity cannot be less than zero")

        self.ingredients[ingredient_type] -= quantity

    @property
    def products(self):
        return self.ingredients
