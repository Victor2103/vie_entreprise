import requests
import json
import os
from dotenv import load_dotenv
load_dotenv(".env")

headers = {'Accept': 'application/json',
           'Authorization': f'Bearer {os.getenv("BEARER_TOKEN")}',
           'nombre': '100'}

url = 'https://api.insee.fr/entreprises/sirene/V3/siren'

data = requests.get(url=url, headers=headers)

# print(data.json())

with open("my_data/insee.json", "w") as f:
    json.dump(data.json(), f)
