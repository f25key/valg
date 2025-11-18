from datetime import datetime
import valglib

print("Velkommen til valg", datetime.now().year)

valgliste = valglib.last_valgliste()

print("For å opprette valg, tast 1. For å fortsette valg, tast 2. For å simulere valg, tast 3.")
print("Hvis du allerede kjeder deg og vil avslutte, tast noe annet. Dette valget er anbefalt.")
option = input("Hva vil du? ")
print(" ")

if option == "1":
    valgnavn = valglib.få_valgnavn()
    if valgnavn in valgliste:
        print("Den finnes allerede, så vi fortsetter på den.")

    valglib.stem_parti(valgnavn, valglib.last_partier())
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
    valgnavn = valglib.få_valgnavn()
    if valgnavn in valgliste:
        if not input(f"{valgnavn} er allerede i systemet. Hvis du er sikker på dette, tast 1. ") == "1":
            exit(0)
    
    valglib.simuler_valg(valgnavn, valglib.last_partier(), int(input("Hvor mange skal stemme? ")))