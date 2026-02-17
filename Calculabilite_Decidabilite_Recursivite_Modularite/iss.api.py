import requests

astronaute = "http://api.open-notify.org/astros.json"
reponse = requests.get(astronaute)

donnees = reponse.json()

print("Nombre de personnes dans l'espace :", donnees["number"])
print("Personnes à bord de l'ISS :")

for personne in donnees["people"]:
    if personne["craft"] == "ISS":
        print(personne["name"])


position = "http://api.open-notify.org/iss-now.json"
rep = requests.get(position)
info = rep.json()

latitude = info["iss_position"]["latitude"]
longitude = info["iss_position"]["longitude"]

print("Position ISS :")
print("Latitude :", latitude)
print("Longitude :", longitude)

