import json
# Import the library for the database.
import psycopg2

import os

cpt = 0
for i in range(0, 40):
    with open(f"my_data/insee_{i}.json", "r") as f:
        data = json.load(f)
    for j in data["unitesLegales"]:
        cpt += 1
        print(j["siren"])
        print(j["nombrePeriodesUniteLegale"])
        print(j["dateCreationUniteLegale"])
        if j["categorieEntreprise"]:
            print(j["categorieEntreprise"])
            print(j["anneeCategorieEntreprise"])
print(cpt)

# Make a connection to the postgresql database
# Connect to the database
connection = psycopg2.connect(
    f"postgres://{str(os.getenv('USERNAME'))}:{str(os.getenv('PASSWORD'))}@postgresql-2791bab0-od486479f.database.cloud.ovh.net:20184/electric?sslmode=require")
cursor = connection.cursor()


# print(data["unitesLegales"][0]['siren'])
