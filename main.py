from datetime import datetime
print("Velkommen til valg", datetime.now().year)

partier = []
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
print("Uimplementert!")