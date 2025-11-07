import random
import json
import os
import re

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