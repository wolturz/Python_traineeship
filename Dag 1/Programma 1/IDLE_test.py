##bestandsnaam = "woorden.txt"
##modus = 'rt'
##woordenbestand = open(bestandsnaam,modus)
##woordenlijst = woordenbestand.read().splitlines()       # splitlines haalt '\n' wel weg, readlines() niet
##woordenset = set(woordenlijst)
##
##def isPalindrome(s):
##    return s == s[::-1]
##
##langste_woord = ''
##for woord in woordenlijst:              # elke lengte van het woord vergelijken of het langer is, zo ja, dan is dit het nieuwe langste woord
##    if len(woord) > len(langste_woord):
##        langste_woord = woord
##
##palindroom_lijst = []
##
##for woord in woordenlijst:              # opzoeken of een woord een palindroom is
##    if isPalindrome(woord) and len(woord) > 1:
##        palindroom_lijst.append(woord)
##
##omgekeerd_lijst = []
##
##for wrd in woordenset:
##    if wrd[::-1] in woordenset and isPalindrome(wrd) == False:
##        omgekeerd_lijst.append(wrd)
##
##print(f"Het aantal woorden in de lijst is {len(woordenlijst)}")
##print(f"Het langste woord is {langste_woord} en heeft een lengte van {len(langste_woord)} letters")
##print("lijst met palindromen:")
##print(palindroom_lijst)
##print("lijst met omgekeerde woorden (exclusief palindromen)")
##print(omgekeerd_lijst)


from random import randint
from random import choice


# Initialisatie
aantal_dozen = 5
kat_doos = randint(1,aantal_dozen)
ronde_nummer = 0
kat_gevonden = False
plus_min_tupel = (-1,1)


# Start van de simulatie
while not kat_gevonden:
    doos_te_openen = int(input("Kies een doosnummer: "))
    ronde_nummer += 1
    if doos_te_openen == kat_doos:
        print(f"Raak! Je hebt {ronde_nummer} pogingen nodig gehad")
        print(f"De kat zat in doos {kat_doos}")
        kat_gevonden = True
    else: print("Mis!")

    if kat_doos == 1:
        kat_doos = 2
    elif kat_doos == 5:
        kat_doos = 4
    else:
        kat_doos = kat_doos + choice(plus_min_tupel)
        
