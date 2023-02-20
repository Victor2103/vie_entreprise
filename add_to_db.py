import json
# Import the library for the database.
import psycopg2

import os

from dotenv import load_dotenv
load_dotenv(".env")

# Make a connection to the postgresql database
# Connect to the database
connection = psycopg2.connect(
    f"postgres://{str(os.getenv('USERNAME'))}:{str(os.getenv('PASSWORD'))}@postgresql-2791bab0-od486479f.database.cloud.ovh.net:20184/vie_entreprise?sslmode=require")
cursor = connection.cursor()

cpt = 0
for i in range(0, 40):
    with open(f"my_data/insee_{i}.json", "r") as f:
        data = json.load(f)
    for j in data["unitesLegales"]:
        cpt += 1
        if j["categorieEntreprise"]:
            cursor.execute(
                "INSERT INTO brand (siren,number_legal_units,date_creation,categorie_entreprise,annee_categorie_entreprise) VALUES (%s,%s,%s,%s,%s); ", (j["siren"], j["nombrePeriodesUniteLegale"], j["dateCreationUniteLegale"], j["categorieEntreprise"], j["anneeCategorieEntreprise"]))
        else:
            cursor.execute(
                "INSERT INTO brand (siren,number_legal_units,date_creation) VALUES (%s,%s,%s); ", (j["siren"], j["nombrePeriodesUniteLegale"], j["dateCreationUniteLegale"]))


print(f"{cpt} have been added ! ")


# This is for make the data saved in the database.
connection.commit()

# Close the database
cursor.close()
connection.close()
