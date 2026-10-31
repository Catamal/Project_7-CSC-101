# CSV preparation:
# import csv
# from pathlib import Path
#
# source = Path("pokemon.csv")
# destination = Path("pokemon_cleaned.csv")
# with source.open(newline="", encoding="utf-8-sig") as input_file:
#     reader = csv.DictReader(input_file)
#     headers = reader.fieldnames or []
#     classification_field = (
#         "classification" if "classification" in headers else "classfication"
#     )
#     rows = [
#         {
#             "abilities": row["abilities"].replace(",", ";"),
#             "name": row["name"],
#             "classification": row[classification_field],
#         }
#         for row in reader
#     ]
#
# with destination.open("w", newline="", encoding="utf-8") as output_file:
#     writer = csv.DictWriter(
#         output_file, fieldnames=["abilities", "name", "classification"]
#     )
#     writer.writeheader()
#     writer.writerows(rows)