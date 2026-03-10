import requests
from collections.abc import Iterator


class BasePokemon:
    name: str

    def __init__(self,name: str) -> None:
        self.name = name

    def __str__(self):
        return f'name={self.name}'


class Pokemon(BasePokemon):
    name: str
    id: str
    height: str
    weight: str

    def __init__(self, name: str, id: str, height: str, weight: str) -> None:
        BasePokemon.__init__(self, name)
        self.__name = self.name
        self.__id = id
        self.__height = height
        self.__weight = weight

    @property
    def names(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    def __str__(self):
        return f'name={self.__name}, id={self.__id}, height={self.__height}, weight={self.__weight}'


class PokeAPI:
    name_id: str
    max_counter: int

    def get_pokemon(self, name_id: str) -> Pokemon:
        for i in range(len(pokeball)):
            if pokeball[i].name == name_id or pokeball[i].id == name_id:
                return pokeball[i]
        else:
            url = "https://pokeapi.co/api/v2/pokemon/" + name_id + "/"
            result = requests.get(url).json()
            pokeball.append(Pokemon(result["name"], result["id"], result["height"], result["weight"]))
            return Pokemon(result["name"], result["id"], result["height"], result["weight"])

    def get_all(self, max_counter: int, get_full=False) -> Iterator:
        counter: int = 1
        while counter <= max_counter:
            url = "https://pokeapi.co/api/v2/pokemon/" + str(counter) + "/"
            result = requests.get(url).json()
            if get_full == False:
                yield BasePokemon(result["name"])
            else:
                yield Pokemon(result["name"], result["id"], result["height"], result["weight"])
            counter += 1


pokeball = []
maxx_weight: int = 0

print(PokeAPI().get_pokemon("ditto"))

for i in PokeAPI().get_all(50, True):
    if maxx_weight < i.weight:
        maxx_weight = i.weight
        pok = i
print(pok)