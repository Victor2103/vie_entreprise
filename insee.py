import requests
import json
import os
from dotenv import load_dotenv
load_dotenv(".env")

headers = {'Accept': 'application/json',
           'Authorization': f'Bearer {os.getenv("BEARER_TOKEN")}',
           'nombre': '10000'}

for i in range(10):
    url = f'https://api.insee.fr/entreprises/sirene/V3/siren?q=dateCreationUniteLegale:[198{i} TO 198{i+1}]'
    data = requests.get(url=url, headers=headers)
    print(data)
    # print(data.json())
    with open(f"my_data/insee_{i}.json", "w") as f:
        json.dump(data.json(), f)

for i in range(10):
    url = f'https://api.insee.fr/entreprises/sirene/V3/siren?q=dateCreationUniteLegale:[199{i} TO 199{i+1}]'
    data = requests.get(url=url, headers=headers)
    print(data)
    # print(data.json())
    with open(f"my_data/insee_{i+10}.json", "w") as f:
        json.dump(data.json(), f)

for i in range(10):
    url = f'https://api.insee.fr/entreprises/sirene/V3/siren?q=dateCreationUniteLegale:[200{i} TO 200{i+1}]'
    data = requests.get(url=url, headers=headers)
    print(data)
    # print(data.json())
    with open(f"my_data/insee_{i+20}.json", "w") as f:
        json.dump(data.json(), f)

for i in range(10):
    url = f'https://api.insee.fr/entreprises/sirene/V3/siren?q=dateCreationUniteLegale:[201{i} TO 201{i+1}]'
    data = requests.get(url=url, headers=headers)
    print(data)
    # print(data.json())
    with open(f"my_data/insee_{i+30}.json", "w") as f:
        json.dump(data.json(), f)
