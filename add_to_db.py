import json

with open("test.json","r") as f:
    data=json.load(f)


# get the siren
tmp=json.loads(data["records"][1]["fields"]["listepersonnes"])
siren=tmp['personne']['numeroImmatriculation']['numeroIdentification']

print(siren)