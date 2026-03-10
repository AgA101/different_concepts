import requests


#url = "https://pokeapi.co/api/v2/pokemon/ditto"


#print(result['height'])
#print(result["weight"])
class BasePokemon:
    def __init__(self,name):
        self.__name = name
    def __str__(self):
        return self.__name

class Pokemon(BasePokemon):
    def __init__(self, name, id, height, weight):
        BasePokemon.__init__(self,name)
        self.__id = id
        self.__height = height
        self.__weight = weight


class PokeAPI:
    def get_pokemon(self,name_id):
        url = "https://pokeapi.co/api/v2/pokemon/" + name_id + "/"
        result = requests.get(url).json()
        return result["name"]



b = BasePokemon(PokeAPI().get_pokemon("345"))
print(b)