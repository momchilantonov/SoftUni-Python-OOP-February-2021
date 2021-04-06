# from customer import Customer
# from dvd import DVD


from project.customer import Customer
from project.dvd import DVD
# from project.move_world import MovieWorld


class MovieWorld:
    DVD_CAP = 15
    CUSTOMER_CAP = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAP

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAP

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAP:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld.DVD_CAP:
            self.dvds.append(dvd)

    def get_current_customer(self, customer_id):
        return [c for c in self.customers if c.id == customer_id][0]

    def get_current_dvd(self, dvd_id):
        return [d for d in self.dvds if d.id == dvd_id][0]

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.get_current_customer(customer_id)
        dvd = self.get_current_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_current_customer(customer_id)
        dvd = self.get_current_dvd(dvd_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += customer.__repr__()+"\n"
        for dvd in self.dvds:
            result += dvd.__repr__()+"\n"
        return result.strip()


# c1 = Customer("John", 16, 1)
# c2 = Customer("Anna", 55, 2)
#
# d1 = DVD("Black Widow", 1, 2020, "April", 18)
# d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)
#
# movie_world = MovieWorld("The Best Movie Shop")
#
# movie_world.add_customer(c1)
# movie_world.add_customer(c2)
#
# movie_world.add_dvd(d1)
# movie_world.add_dvd(d2)
#
# print(movie_world.rent_dvd(1, 1))
# print(movie_world.rent_dvd(2, 1))
# print(movie_world.rent_dvd(1, 2))
#
# print(movie_world)
