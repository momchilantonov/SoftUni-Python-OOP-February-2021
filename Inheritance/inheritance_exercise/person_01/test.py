from Inheritance.inheritance_exercise.person_01.project.person import Person
from Inheritance.inheritance_exercise.person_01.project.child import Child


person = Person("Peter", 25)
print(person.name)
print(person.age)
print(person.__class__.__name__)
print("________")
child = Child("Peter Junior", 5)
print(child.name)
print(child.age)
print(child.__class__.__name__)
print(child.__class__.__bases__[0].__name__)
