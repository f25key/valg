from datetime import datetime
import glob
import os
import re

if not os.path.isdir("valgdata"):
    if os.path.exists("valgdata"):
        print("Du har en fil som heter 'valgdata' i denne mappen.")
        exit(1)
    os.mkdir("valgdata")
print("Velkommen til valg", datetime.now().year)

partier = []
valgliste = [os.path.basename(os.path.dirname(vlg)) for vlg in glob.glob("valgdata/*/")]

with open("partier.txt") as partier_fil:
    for parti in partier_fil.read().splitlines():
        try:
            partier.append([parti.split(",")[0], float(parti.split(",")[1])])
        except Exception as e:
            print("Noe er galt med partier.txt:", e)
            print("Dette partiet førte til feilen:", parti)
            exit(1)

print("For å opprette valg, tast 1. For å fortsette valg, tast 2. For å simulere valg, tast 3.")
print("Hvis du allerede kjeder deg og vil avslutte, tast noe annet. Dette valget er anbefalt.")
option = input("Hva vil du? ")
print(" ")

def start_valg(valgnavn):
    print(" ")
    partinavn = [x[0].lower() for x in partier]
    print("Vi har disse partiene:", partinavn)
    stem = input("Hvem stemmer du for? ").lower()

    if not stem in partinavn:
        print("Beklager, det var ikke et parti.")
        exit(1)
    
    # tja, det var snakk om en bruker som stemmer, så da blir det ikke anonymt
    lagre_stemmer({stem:1}, valgnavn)

def lagre_stemmer(stemmer, valgnavn):
    print(stemmer)

if option == "1":
    valgnavn = input("Hva kaller du dette valget? ").lower()
    if re.match(r"[\./<>:\"\\|?*]", valgnavn):
        print("Beklager, du har brukt karakterer i navnet som ikke støttes.")
        exit(1)
    
    os.mkdir("valgdata/"+valgnavn)
    start_valg(valgnavn)
elif option == "2":
    if len(valgliste) == 0:
        print("Du har ingen valg å fortsette på akkurat nå. Opprett valg først.")
        exit(0)
    
    print("Følgende valg er i systemet:", valgliste)
    valgnavn = input("Hvilket valg skal du laste inn? ").lower()
    if not valgnavn in valgliste:
        print("Beklager,", valgnavn, "er ikke i systemet.")

    start_valg(valgnavn)