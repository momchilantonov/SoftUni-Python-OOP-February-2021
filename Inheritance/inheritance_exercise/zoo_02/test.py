from Inheritance.inheritance_exercise.zoo_02.project.mammal import Mammal
from Inheritance.inheritance_exercise.zoo_02.project.lizard import Lizard

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)
