import requests
from RoomExtractor import getRoomURLs
from InfoExtractor import getRoomInfo
from FilterOffers import filterOffers

# FILTERS
sexF = "Man"    # Man or Vrouw
maxPrice = 850
minSurface = 8
includeGWE = False

city = input("Enter city name: ").lower()
sexF = input("Enter sex (Man or Vrouw): ")
maxPrice = int(input("Enter max Price (num): "))
minSurface = int(input("Enter min Surface area (num): "))
includeGWE = input("G,W,E included (Yes or No): ").lower() in ("yes", "true")
print("\n\nResults:\n")

URL = "https://kamernet.nl/huren/kamers-" + city + "/"
roomURLs = getRoomURLs(URL, [maxPrice, minSurface, includeGWE])

for url in roomURLs:
    sex, langs = getRoomInfo(url)
    filterOffers(sex, langs, url, sexF)
    

