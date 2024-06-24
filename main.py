import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium


#recherche de pays
num = "+261339809323"
monNum = phonenumbers.parse(num)
localisation = geocoder.description_for_number(monNum, "fr")
print(localisation)

#trouver l'operateur
operateur = phonenumbers.parse(num)
print(carrier.name_for_number(operateur, "fr"))

#trouver le latitude et longitude
clef = "0fe3fb0728934d69946c2ea54f3ffbbc"
coord = OpenCageGeocode(clef)
requete = str(localisation)
reponse = coord.geocode(requete)
lat = reponse[0]['geometry']['lat']
lng = reponse[0]['geometry']['lng']

print(lat, lng)

#affichage sur la carte
monMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=localisation).add_to(monMap)
monMap.save("monMap.html")