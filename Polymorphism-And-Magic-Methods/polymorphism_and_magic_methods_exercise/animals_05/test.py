from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.animals_05.project.dog import Dog
from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.animals_05.project.cat import Cat
from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.animals_05.project.kitten import Kitten
from PolymorphismAndMagicMethods.polymorphism_and_magic_methods_exercise.animals_05.project.tomcat import Tomcat

dog = Dog("Yarik", 3, "Male")
print(dog.make_sound())
print(dog.__repr__())

cat = Cat("Pisana", 2, "Female")
print(cat.make_sound())
print(cat.__repr__())

kitty = Kitten("Miss", 3)
print(kitty.make_sound())
print(kitty.__repr__())

tom = Tomcat("Tom", 5)
print(tom.make_sound())
print(tom.__repr__())
