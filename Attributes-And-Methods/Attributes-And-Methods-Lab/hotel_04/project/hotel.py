from room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, start_count):
        return cls(f"{start_count} stars Hotel")

    def get_room_by_number(self, room_number):
        return [room for room in self.rooms if room.number == room_number][0]

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = self.get_room_by_number(room_number)
        result = room.take_room(people)
        if result:
            return result
        self.guests += people

    def free_room(self, room_number):
        room = self.get_room_by_number(room_number)
        guests_for_remove = room.guests
        result = room.free_room()
        if result:
            return result
        self.guests -= guests_for_remove

    def print_status(self):
        free_rooms = [room for room in self.rooms if not room.is_taken]
        taken_rooms = [room for room in self.rooms if room.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(str(room.number) for room in free_rooms)}")
        print(f"Taken rooms: {', '.join(str(room.number) for room in taken_rooms)}")


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)
hotel.print_status()

hotel.free_room(1)
hotel.free_room(3)
hotel.print_status()
