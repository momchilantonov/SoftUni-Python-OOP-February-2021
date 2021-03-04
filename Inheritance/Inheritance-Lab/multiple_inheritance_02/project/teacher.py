from person import Person
from employee import Employee


class Teacher(Person, Employee):

    @staticmethod
    def teach():
        return "teaching..."


teacher = Teacher()
print(teacher.teach())
print(teacher.sleep())
print(teacher.get_fired())