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
        for k in j["periodesUniteLegale"]:
            if k["nicSiegeUniteLegale"]:
                cursor.execute("INSERT INTO legal_units (siren,siret,administrative_state,change_state,start_date,end_date,nomenclature_activite,changement_activite) VALUES (%s,%s,%s,%s,%s,%s,%s,%s) ;", (
                               j["siren"], j["siren"]+k["nicSiegeUniteLegale"], k["etatAdministratifUniteLegale"], k["changementEtatAdministratifUniteLegale"], k["dateDebut"], k["dateFin"], k["nomenclatureActivitePrincipaleUniteLegale"], k["changementActivitePrincipaleUniteLegale"]))
            else:
                cursor.execute("INSERT INTO legal_units (siren,administrative_state,change_state,start_date,end_date,nomenclature_activite,changement_activite) VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                               j["siren"], k["etatAdministratifUniteLegale"], k["changementEtatAdministratifUniteLegale"], k["dateDebut"], k["dateFin"], k["nomenclatureActivitePrincipaleUniteLegale"], k["changementActivitePrincipaleUniteLegale"]))

# This is for make the data saved in the database.
connection.commit()


# Close the database
cursor.close()
connection.close()
