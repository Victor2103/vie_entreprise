import requests
import os
from dotenv import load_dotenv
import pandas as pd
import json
load_dotenv(".env")


body = {"username": str(os.getenv("NAME")),
        "password": str(os.getenv("PASSWORD"))}

print(str(os.getenv("NAME")))
print(str(os.getenv("PASSWORD")))

x = requests.post(
    "https://registre-national-entreprises-pprod.inpi.fr/api/sso/login", json=body)

print(x.text)

data = pd.read_excel("my_data/if155.xls")

print(data)

y = requests.get("https://bodacc-datadila.opendatasoft.com/api/records/1.0/search/?dataset=annonces-commerciales&q=Siren&facet=publicationavis&facet=publicationavis_facette&facet=typeavis&facet=typeavis_lib&facet=familleavis&facet=familleavis_lib&facet=numerodepartement&facet=departement_nom_officiel&refine.familleavis_lib=Ventes+et+cessions")
# print(y.text)


z = requests.get('https://bodacc-datadila.opendatasoft.com/api/records/1.0/search/?dataset=annonces-commerciales&q=&rows=100&sort=dateparution&facet=publicationavis&facet=publicationavis_facette&facet=typeavis&facet=typeavis_lib&facet=familleavis&facet=familleavis_lib&facet=numerodepartement&facet=departement_nom_officiel&refine.departement_nom_officiel=Alpes-Maritimes&refine.familleavis_lib=Radiations&refine.typeavis_lib=Avis+d%E2%80%99annulation')

# Transform into a json file
data = z.json()

print(data["records"][1]["fields"])

with open("test.json", "w") as f:
    json.dump(data, f)
