import random
import json
import os
import re

def last_partier():
    """Laster inn og returnerer partiene fra partifilen."""
    partier = []
    with open("partier.txt") as partier_fil:
        for parti in partier_fil.read().splitlines():
            try:
                if '"' in parti:
                    print("Ikke bruk anførselstegn, som i:", parti)
                    exit(1)

                partinavn = parti.split(",")[0]
                partiandel = float(parti.split(",")[1])
                partier.append((partinavn, partiandel))
            except Exception as e:
                print("Noe er galt med partier.txt:", e)
                print("Dette partiet førte til feilen:", parti)
                exit(1)

    return partier

def få_valgnavn():
    """Be brukeren om et valgnavn. Karakterer som ikke støttes på Windows eller
    som kan brukes for å traversere mapper er forbudt."""

    valgnavn = input("Hva kaller du dette valget? ").lower()
    if re.match(r"[\./<>:\"\\|?*]", valgnavn):
        print("Beklager, du har brukt karakterer i navnet som ikke støttes.")
        exit(1)
    return valgnavn

def stem_parti(valgnavn, partier):
    """Be brukeren stemme på et parti, også lagre stemmen."""
    print(" ")
    partinavn = [x[0].lower() for x in partier]
    random.shuffle(partinavn)

    print("Vi har disse partiene:", partinavn)
    stem = input("Hvem stemmer du for? ").lower()
    if not stem in partinavn:
        print("Beklager, det var ikke et parti.")
        exit(1)
    
    # tja, det var snakk om en bruker som stemmer, så da blir det ikke anonymt
    lagre_stemmer({stem:1}, valgnavn)

def lagre_stemmer(stemmer, valgnavn):
    """Lagrer stemmen med å laste inn forrige stemmer fra en fil også skrive til den."""
    filbane = f"valgdata/{valgnavn}.json"
    
    if os.path.exists(filbane):
        valgdata = json.load(open(filbane))
    else:
        valgdata = {}
    
    for parti, stemmer in stemmer.items():
        valgdata[parti] = valgdata.get(parti,0) + stemmer
    
    json.dump(dict(sorted(valgdata.items())), open(filbane, "w"), ensure_ascii=False, indent=2)
    print("Lagret.")