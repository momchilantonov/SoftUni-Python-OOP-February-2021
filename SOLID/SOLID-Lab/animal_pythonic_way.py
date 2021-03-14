sound_mapper = {
    "cat": "meow",
    "dog": "woof_woof",
    "chicken": "chuch",
}


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


def animal_sound(animals):
    for animal in animals:
        try:
            print(sound_mapper[animal.species.lower()])
        except:
            print("Unknown sound")


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)
