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


# The command to create the table brand with all the infos of the brand
command = """
        CREATE TABLE brand (
            siren VARCHAR(9) NOT NULL ,
            number_legal_units INTEGER NOT NULL ,
            date_creation TIMESTAMPTZ NOT NULL ,
            categorie_entreprise VARCHAR(255) NULL ,
            annee_categorie_entreprise VARCHAR(4) NULL 
        );
        """

# The command to create the table of all legals units for the brand.
command2 = """
        CREATE TABLE legal_units (
            siren VARCHAR(9) NOT NULL ,
            siret VARCHAR(14) NULL ,
            administrative_state VARCHAR(1) NOT NULL,
            change_state BOOLEAN NOT NULL ,
            start_date TIMESTAMPTZ NOT NULL ,
            end_date TIMESTAMPTZ NOT NULL, 
            nomenclature_activite VARCHAR(255) NOT NULL ,
            changement_activite BOOLEAN NOT NULL 
        )
"""

# Add the table to the database
cursor.execute(command)

# Add the other table to the database
cursor.execute(command2)

# Save in the database
connection.commit()

# Close the database
cursor.close()
connection.close()
