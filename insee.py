import requests
import json

headers = {'Accept': 'application/json',
           'Authorization': 'Bearer de96c85b-a5b6-3ceb-a32c-4c0bdfc87e09'}

url = 'https://api.insee.fr/entreprises/sirene/V3/siren'

data = requests.get(url=url, headers=headers)

# print(data.json())

with open("my_data/insee.json", "w") as f:
    json.dump(data.json(), f)
