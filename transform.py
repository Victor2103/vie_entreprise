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

cursor.execute("SELECT siren FROM brand WHERE number_legal_units > 1 ;")


# print(cursor.fetchall())
sirens = cursor.fetchall()
cursor.close()
cursor = connection.cursor()
# print(sirens[0][0])
for i in range(len(sirens)):
    cursor.execute(
        "SELECT start_date,end_date,siren FROM legal_units WHERE siren=%s ;", [sirens[i][0]])
    # print(cursor.fetchall())


# Close the database
cursor.close()
connection.close()
