class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {self.is_dvd_rented()}"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        month_mapper = {
            "01": "January",
            "02": "February",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December"
        }
        day, month, year = date.split(".")
        return cls(name, id, int(year), month_mapper[month], age_restriction)

    def is_dvd_rented(self):
        if self.is_rented:
            return "rented"
        return "not rented"
