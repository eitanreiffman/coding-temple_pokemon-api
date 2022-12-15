import requests

class PokemonAPI:
    base_url = "https://pokeapi.co/api/v2/"

    def __init__(self, pokemon_name, height=0, weight=0):
        self.pokemon_name = pokemon_name
        self.height = height
        self.weight = weight

    def _get(self):
        request_url = f"{self.base_url}/pokemon/{self.pokemon_name}"
        poke_response = requests.get(request_url)
        if poke_response.ok:
            poke_dict = poke_response.json()
            self.height = poke_dict["height"]
            self.weight = poke_dict["weight"]
            print(f"{self.pokemon_name.title()} has a height of {self.height} decimeters and a weight of {self.weight} hectograms.")

        else:
            print("Error")


pokemon1 = PokemonAPI('onix')
pokemon2 = PokemonAPI('snorlax')
pokemon3 = PokemonAPI('blastoise')

pokemon1._get()
print("="*50)
pokemon2._get()
print("="*50)
pokemon3._get()