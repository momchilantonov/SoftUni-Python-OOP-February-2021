from customer import Customer
from dvd import DVD


class MovieWorld:
    dvd_cap = 15
    customer_cap = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.dvd_cap

    @staticmethod
    def customer_capacity():
        return MovieWorld.customer_cap

    def is_customer_valid(self, customer):
        return customer not in self.customers \
               and len(self.customers) < MovieWorld.customer_cap

    def is_dvd_valid(self, dvd):
        return dvd not in self.dvds \
               and len(self.dvds) < MovieWorld.dvd_cap

    def add_customer(self, customer):
        if self.is_customer_valid(customer):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.is_dvd_valid(dvd):
            self.dvds.append(dvd)

    def get_customer(self, customer_id):
        return [c for c in self.customers if c.id == customer_id][0]

    def get_dvd(self, dvd_id):
        return [d for d in self.dvds if d.id == dvd_id][0]

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.get_customer(customer_id)
        dvd = self.get_dvd(dvd_id)
        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.get_customer(customer_id)
        dvd = self.get_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += customer.__repr__()+"\n"
        for dvd in self.dvds:
            result += dvd.__repr__()+"\n"
        return result


c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world.dvd_capacity())

print(movie_world)
