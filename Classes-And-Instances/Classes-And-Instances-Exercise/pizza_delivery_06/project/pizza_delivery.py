class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = dict(ingredients)
        self.ordered = False

    def add_extra(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = quantity
            self.price += quantity * ingredient_price
        else:
            self.ingredients.update({ingredient: self.ingredients[ingredient]+quantity})
            self.price += quantity * ingredient_price

    def remove_ingredient(self, ingredient, quantity, ingredient_price):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient in self.ingredients:
            if self.ingredients[ingredient] >= quantity:
                self.ingredients.update({ingredient: self.ingredients[ingredient]-quantity})
                self.price -= quantity * ingredient_price
                return
            return f"Please check again the desired quantity of {ingredient}!"
        return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with " \
               f"{', '.join((': '.join((str(i), str(q)))) for i, q in self.ingredients.items())} " \
               f"and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
