import requests
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv(".env")


body = {"username": str(os.getenv("NAME")),
        "password": str(os.getenv("PASSWORD"))}

print(str(os.getenv("NAME")))
print(str(os.getenv("PASSWORD")))

x = requests.post(
    "https://registre-national-entreprises-pprod.inpi.fr/api/sso/login", json=body)

print(x.text)

data=pd.read_csv("my_data/if155.xls")

print(data)