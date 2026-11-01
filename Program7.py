# Program 7: Catch em all!
# 10/28/26
# Kingsley Wickstrom
# Loads Pokemon from a CSV and lets the user search by name.


import csv  # helps read csv files
import sys  # lets the program configure text output
from pathlib import Path  # Builds a path to the CSV beside this script.
from typing import List, Optional  # Describes list and optional return types.

# New Python functions/terminology I learned:
# reconfigure() sets the output encoding to UTF-8
# 

# casefold() makes text lowercase for case-insensitive comparisons
# NOTE: this is not required but it can be useful for weird cases
# when comparing str or filtering
# (ex. Straße means street in german; ß is outputted as ss in casefold
# as it breaks the character down to its standardized layout because
# it is equivalent to ss while lower keeps the ß)  

# @property lets a method be used like an attribute.
# @setter lets an attribute assignment update its stored value.

# in some lines I use type hints 
# ex. abilities: str 
# this type of hint is to acknowledge its meant to be a str 
# ex. -> None; -> str
# this type of hint shows whether a function needs to display 
# a useful value; None = it isn't meant to


class Pokemon:
    """Store a Pokemon's abilities, classification, and name."""

    def __init__(self, abilities: str, classification: str, name: str) -> None:
        # attributes that are stored when recalling information
        self._abilities = abilities
        self._classification = classification
        self._name = name

    @property # access abilities
    def abilities(self) -> str:
        return self._abilities

    @abilities.setter # assign abilities
    def abilities(self, abilities: str) -> None:
        self._abilities = abilities

    @property # access classification
    def classification(self) -> str:
        return self._classification

    @classification.setter # assign classification
    def classification(self, classification: str) -> None:
        self._classification = classification

    @property # access name
    def name(self) -> str:
        return self._name

    @name.setter # assign name
    def name(self, name: str) -> None:
        self._name = name


def load_pokemon(source: Path) -> List[Pokemon]:
    """Load the selected columns from the Pokemon CSV."""
    with source.open(newline="", encoding="utf-8-sig") as pokemon_file:
        reader = csv.DictReader(pokemon_file)
        fields = reader.fieldnames or []
        required_fields = {"abilities", "name", "classification"}
        if not required_fields.issubset(fields):
            raise ValueError("pokemon.csv is missing a required field")

        pokemon_list = [
            Pokemon(
                abilities = row["abilities"].replace(",", ";"),
                classification = row["classification"],
                name = row["name"],
            )
            for row in reader
        ]

    pokemon_list.sort(key=lambda pokemon: pokemon.name.casefold())
    return pokemon_list


def binary_search(pokemon_list: List[Pokemon], name: str) -> Optional[Pokemon]:
    """Find a Pokemon by name in a list sorted by name."""
    target = name.casefold()
    i = 0
    j = len(pokemon_list) - 1

    while i <= j:
        mid = (i + j) // 2
        current_name = pokemon_list[mid].name.casefold()
        if current_name == target:
            return pokemon_list[mid] # pokemon found
        if current_name < target:
            i = mid + 1
        else:
            j = mid - 1

    return None # no pokemon found


def main() -> None:
    source = Path(__file__).with_name("pokemon.csv")
    sys.stdout.reconfigure(encoding="utf-8") # used for encoding the output
    pokemon_list = load_pokemon(source)
    print(f"Loaded {len(pokemon_list)} Pokemon.")

    while True:
        search_name = input("Enter a Pokémon name to look up (or Q to quit): "
                            ).strip()
        if search_name.casefold() == "q":
            print("Goodbye!")
            break

        result = binary_search(pokemon_list, search_name)
        if result is None:
            print(f"{search_name} was not found.")
        else:
            print(f"Abilities: {result.abilities}")
            print(f"Classification: {result.classification}")


main()
