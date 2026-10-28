import csv
import sys
from pathlib import Path


def main():
    source = Path(__file__).with_name("pokemon.csv")
    sys.stdout.reconfigure(encoding="utf-8", newline="")

    with source.open(newline="", encoding="utf-8") as pokemon_file:
        pokemon = csv.DictReader(pokemon_file)
        required_fields = {"abilities", "name", "classfication"}
        if not required_fields.issubset(pokemon.fieldnames or []):
            raise ValueError("pokemon.csv is missing a required field")

        output = csv.writer(sys.stdout)
        output.writerow(["abilities", "name", "classification"])
        for row in pokemon:
            output.writerow(
                [row["abilities"], row["name"], row["classfication"]]
            )


if __name__ == "__main__":
    main()