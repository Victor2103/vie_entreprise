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

create_table = """
        CREATE TABLE stat_0_400 (
            interval VARCHAR(20) NOT NULL ,
            value INTEGER NOT NULL
        )
"""

cursor.execute(create_table)
inf = 0
sup = 10
for i in range(40):
    inf += 10
    sup += 10
    cursor.execute(
        "SELECT count(diff) FROM difference WHERE diff >= %s AND diff < %s AND change_state='t' ;", (inf, sup))
    count = cursor.fetchone()
    cursor.execute("INSERT INTO stat_0_400 (interval,value) VALUES (%s,%s)",
                   (f"{inf} - {sup}", count[0]))

connection.commit()

# Close the database
cursor.close()
connection.close()
