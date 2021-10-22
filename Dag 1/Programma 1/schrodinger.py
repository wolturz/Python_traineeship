from random import randint
from random import choice

# Initialisatie
aantal_dozen = 5
kat_doos = randint(1,aantal_dozen)
ronde_nummer = 0
kat_gevonden = False
plus_min_tupel = (-1,1)     # tupel voor de random keuze tussen +1 en -1 bij kat verplaatsen

# Start van de simulatie
while not kat_gevonden:     # zolang de kat niet gevonden is, dus als de waarde False is, blijft het draaien
    doos_te_openen = int(input("Kies een doosnummer tussen 1 en 5: "))
    
    while doos_te_openen > 5:       # te grote getallen eruit filteren
        print("Gelieve 1, 2, 3, 4 of 5 invullen")
        doos_te_openen = int(input("Nu wel goed kiezen!: "))
    while doos_te_openen < 1:       # te kleine getallen eruit filteren
        print("Gelieve 1, 2, 3, 4 of 5 invullen")
        doos_te_openen = int(input("Nu wel goed kiezen!: "))
   
    ronde_nummer += 1               # tellertje met 1 ophogen
    
    if doos_te_openen == kat_doos:      # als gekozen doos en kat doos gelijk zijn, dan print en kat_gevonden true zodat while loop afsluit
        print(f"Raak! Je hebt {ronde_nummer} pogingen nodig gehad")
        print(f"De kat zat in doos {kat_doos}")
        kat_gevonden = True
    else: print("Mis!")

    if kat_doos == 1:                   # waarde voor 1 is apart, alleen ophogen dan
        kat_doos += 1
    elif kat_doos == 5:                 # waarde voor 5 is apart, alleen verminderen dan
        kat_doos -= 1
    else:
        kat_doos = kat_doos + choice(plus_min_tupel)    # kat doos nummer waar -1 of 1 bij opgeteld wordt, is een random keuze