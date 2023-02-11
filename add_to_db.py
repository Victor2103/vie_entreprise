import json

with open("my_data/insee.json", "r") as f:
    data = json.load(f)

"""
# get the siren
tmp=json.loads(data["records"][1]["fields"]["listepersonnes"])
siren=tmp['personne']['numeroImmatriculation']['numeroIdentification']

print(siren)
"""

print(data["unitesLegales"][0]['siren'])
