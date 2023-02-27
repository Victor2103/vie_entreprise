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


# command to add the extension time scaledb or timestamptz
extension = 'CREATE EXTENSION IF NOT EXISTS timescaledb;'


# Create the database and add extension
cursor.execute(extension)

# Command to save in the cluster the change
connection.commit()
# Close the database
cursor.close()
connection.close()
