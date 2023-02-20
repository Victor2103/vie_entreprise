import json

cpt = 0
for i in range(0, 40):
    with open(f"my_data/insee_{i}.json", "r") as f:
        data = json.load(f)
    for j in data["unitesLegales"]:
        cpt += 1
        print(j["siren"])
        print(j["nombrePeriodesUniteLegale"])
        print(j["dateCreationUniteLegale"])
        if j["categorieEntreprise"]:
            print(j["categorieEntreprise"])
print(cpt)
# print(data["unitesLegales"][0]['siren'])
