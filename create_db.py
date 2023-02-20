# Import the library for the database.
import psycopg2

import os

from dotenv import load_dotenv
load_dotenv(".env")

# Make a connection to the postgresql database
# Connect to the database
connection = psycopg2.connect(
    f"postgres://{str(os.getenv('USERNAME'))}:{str(os.getenv('PASSWORD'))}@postgresql-2791bab0-od486479f.database.cloud.ovh.net:20184/electric?sslmode=require")
cursor = connection.cursor()


# The command to create the database vie_entreprise
command = 'CREATE DATABASE vie_entreprise'


# Set the auto commit to avoid an error
auto_comit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
connection.set_isolation_level(auto_comit)


# Create the database and add extension
cursor.execute(command)

# Command to save in the cluster the change
connection.commit()
# Close the database
cursor.close()
connection.close()
