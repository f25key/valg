from datetime import datetime
import valglib
import glob
import os

if not os.path.isdir("valgdata"):
    if os.path.exists("valgdata"):
        print("Du har en fil som heter 'valgdata' i denne mappen.")
        exit(1)
    os.mkdir("valgdata")

print("Velkommen til valg", datetime.now().year)

valgliste = [os.path.splitext(os.path.basename(vlg))[0] for vlg in glob.glob("valgdata/*.json")]

print("For å opprette valg, tast 1. For å fortsette valg, tast 2. For å simulere valg, tast 3.")
print("Hvis du allerede kjeder deg og vil avslutte, tast noe annet. Dette valget er anbefalt.")
option = input("Hva vil du? ")
print(" ")

if option == "1":
    valglib.stem_parti(valglib.få_valgnavn(), valglib.last_partier())
elif option == "2":
    if len(valgliste) == 0:
        print("Du har ingen valg å fortsette på akkurat nå. Opprett valg først.")
        exit(0)
    
    print("Følgende valg er i systemet:", valgliste)
    valgnavn = input("Hvilket valg skal du laste inn? ").lower()
    if not valgnavn in valgliste:
        print("Beklager,", valgnavn, "er ikke i systemet.")
        exit(1)

    valglib.stem_parti(valgnavn, valglib.last_partier())
elif option == "3":
    print("Uimplementert!")