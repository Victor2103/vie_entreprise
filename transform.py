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
tab = []
for i in range(len(sirens)):
    cursor.execute(
        "SELECT start_date,end_date,siren,change_state FROM legal_units WHERE siren=%s ;", [sirens[i][0]])
    # print(cursor.fetchall())
    request = cursor.fetchall()
    for j in range(len(request)):
        if request[j][0] != None and request[j][1] != None:
            # print(request[i][1]-request[i][0])
            tmp = (request[j][2], (request[j][1] -
                   request[j][0]).days, request[j][3])
            tab.append(tmp)
# print(tab)

create_diff = """ CREATE TABLE difference (
    id SERIAL ,
    siren VARCHAR(9) NOT NULL ,
    diff INTEGER NOT NULL  ,
    change_state BOOLEAN NOT NULL
) ;

"""
cursor.execute(create_diff)

for i in range(len(tab)):
    cursor.execute(
        "INSERT INTO difference (siren,diff,change_state) VALUES (%s,%s,%s) ", tab[i])

connection.commit()

# Close the database
cursor.close()
connection.close()
