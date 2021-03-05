from Inheritance.inheritance_exercise.players_and_monsters_03.project.hero import Hero
from Inheritance.inheritance_exercise.players_and_monsters_03.project.elf import Elf
from Inheritance.inheritance_exercise.players_and_monsters_03.project.wizard import Wizard
from Inheritance.inheritance_exercise.players_and_monsters_03.project.knight import Knight
from Inheritance.inheritance_exercise.players_and_monsters_03.project.dark_knight import DarkKnight

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 6)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
dark_knight = DarkKnight("DK", 6)
print(str(dark_knight))
print(dark_knight.__class__.__bases__[0].__name__)
print(dark_knight.username)
print(dark_knight.level)

