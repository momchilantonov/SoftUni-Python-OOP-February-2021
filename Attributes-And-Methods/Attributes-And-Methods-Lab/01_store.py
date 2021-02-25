class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size // 2)

    def can_add_item(self):
        return self.capacity > 0

    def can_remove_item(self, item_name, amount):
        return item_name in self.items and self.items[item_name] >= amount

    def verify_item(self, item_name):
        if item_name not in self.items:
            self.items[item_name] = 0

    def add_item(self, item_name):
        if not self.can_add_item():
            return "Not enough capacity in the store"
        self.verify_item(item_name)
        self.capacity -= 1
        self.items[item_name] += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name, amount):
        if not self.can_remove_item(item_name, amount):
            return f"Cannot remove {amount} {item_name}"
        self.capacity += amount
        self.items[item_name] -= amount
        return f"{amount} {item_name} removed from the store"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
