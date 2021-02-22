from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_collection = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon_collection:
            return "This pokemon is already caught"
        self.pokemon_collection.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemon_collection:
            if pokemon.name == pokemon_name:
                self.pokemon_collection.remove(pokemon)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n" \
                 f"Pokemon count {len(self.pokemon_collection)}\n"
        for pokemon in self.pokemon_collection:
            result += f"- {pokemon.pokemon_details()}\n"
        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
