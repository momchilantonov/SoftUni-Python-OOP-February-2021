class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def can_take_room(self, people):
        return not self.is_taken and self.capacity >= people

    def can_free_room(self):
        return self.is_taken

    def take_room(self, people):
        if not self.can_take_room(people):
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests = people

    def free_room(self):
        if not self.can_free_room():
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0
