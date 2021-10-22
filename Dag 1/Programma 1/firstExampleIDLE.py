##print("hallo allemaal")
##
##a = 5
##print(a)
##b = 3
##print(b)
##
##if a>b:
##    a = b
##    b = c

##i = 0
##k = 0
##
##while i<99:
##    k = k + (i*2) - 1
##
##print(k)
##
##k = 0
##i = 0
##while i<10:
##    i = i + 1
##    k = k + i
##    j = 0
##    while j <10:
##        j = j + 1
##        k = k * j
##
##print(k)

# def fibonaccilijst(aantal_getallen):
#     if aantal_getallen == 0:
#         lijst = []
#     if aantal_getallen == 1:
#         lijst = [0.5]
#     if aantal_getallen >= 2:
#         lijst = [0.5,1]                 # geen waarde 0, de waarde 0.5 is de eerste waarde
#         while len(lijst)<aantal_getallen:
#             if lijst[-1] == 0.5 or lijst[-2] == 0.5:
#                 lijst.append(2)
#             else:
#                 lijst.append(lijst[-1]+lijst[-2])
#     return lijst

# def alternatieve_fibonaccilijst(aantal_getallen):
#     reeks = [0,1]
    
#     while len(reeks) <= aantal_getallen:
#         reeks.append(reeks[len(reeks)-2] + reeks[len(reeks)-1])  

#     reeks[1] = 0.5
#     reeks.remove(0)

#     if aantal_getallen == 0:
#         return []
#     else:
#         return reeks

# assert len(fibonaccilijst(50)) == 50, 'Fout: aantal retour waarden klopt niet'
# assert fibonaccilijst(0) == [], 'Fout: teruggegeven waarden kloppen niet'
# assert fibonaccilijst(1) == [0.5], 'Fout: teruggegeven waarden kloppen niet'
# assert fibonaccilijst(2) == [0.5, 1], 'Fout: teruggegeven waarden kloppen niet'
# assert fibonaccilijst(3) == [0.5, 1, 2], 'Fout: teruggegeven waarden kloppen niet'
# assert fibonaccilijst(4) == [0.5, 1, 2, 3], 'Fout: teruggegeven waarden kloppen niet'
# assert fibonaccilijst(5) == [0.5, 1, 2, 3, 5], 'Fout: teruggegeven waarden kloppen niet'
# print(fibonaccilijst(5))

# from random import choice

# aantal_elementen = 1000
# knikkerbak = set()

# for element in range(0,aantal_elementen):
#     knikkerbak.add(choice(["rood","blauw"]))

# print(len(knikkerbak))

# configuratie = {
#     "processor": "Intel i7 Keylane",
#     "memory": "16GB Kingston DDR5",
#     "ssd": "512 GB"
# }

# print(configuratie["processor"])

# configuratie.update({"processor":"Intel Core i7-8565U"})
# print(configuratie.get("processor"))

# print(configuratie)
# print(configuratie.keys())
# print(configuratie.values())
# print(configuratie.items())

# i = 0
# while i < 10:
#   i = i + 1
#   if i == 5:
#     continue
#   print('i =',i)  # De waarde 5 wordt niet getoond

# i = 0
# while i < 10:
#   i = i + 1
#   if i == 5:
#     break
#   print('i =',i)  # Alleen waardes tot en met 4

# try:
#   f.open("brian.txt")
#   f.write("always look at thebright side!")
# except:
#   print("Er trad een fout op bij het schrijven")
# finally:
#   f.close()

# bestandsnaam = 'tekst.txt'

# modus = 'xt' # aanmaken, create, tekstbestand
# f = open("tekst.txt", modus)
# f.write('een eerste regel tekst in het bestand')
# f.close() # sluit het bestand

# modus='at' # toevoegen, append, tekstbestand
# f = open(bestandsnaam,modus)
# f.write('een nieuwe regel in het bestand')
# f.close() # sluit het bestand

# bestandsnaam = "mijnbestand.txt"    # dubbele quotes zijn okee
# modus = "rt"
# f = open(bestandsnaam,modus)
# while True:
#     regel = f.readline()
#     if regel == None:   # None betekent dat einde bestand is bereikt
#         break   # stop de verdere verwerking
#     print(regel)
# f.close()

# bestandsnaam = 'veelregels.txt'
# mijnbestand = open(bestandsnaam, 'rt')
# mijn_lijst_met_regels = mijnbestand.readlines()
# mijnbestand.close()
# for regel in mijn_lijst_met_regels:
#     print(regel)

# import mijnmodule # importeert alles uit mijn module
# from mijnmodule import dezefunctie
# from mijnmodule import dezefunctie as nieuwefunctie

# q = mijnmodule.diefunctie()
# s = dezefunctie()
# t = nieuwefunctie()

# from time import sleep as pauze     # importeer sleep en hernoem de functie tot pauze
# print("We wachten twee seconden")
# pauze(2)    # de hernoemde sleep functie
# print("En nu zijn we terug")


########################################################################################
# Spelen met woorden
# Wat Python code om alvast aan de slag te kunnen
# Het bestand 'woorden.txt.zip' staat op deze pagina

# bestandsnaam = "woorden.txt"
# modus = 'rt'
# woordenbestand = open(bestandsnaam,modus)
# woordenlijst = woordenbestand.read().splitlines()       # splitlines haalt '\n' wel weg, readlines() niet
# woordenset = set(woordenlijst)

# def isPalindrome(s):
#     return s == s[::-1]

# langste_woord = ''
# for woord in woordenlijst:              # elke lengte van het woord vergelijken of het langer is, zo ja, dan is dit het nieuwe langste woord
#     if len(woord) > len(langste_woord):
#         langste_woord = woord

# palindroom_lijst = []

# for woord in woordenlijst:              # opzoeken of een woord een palindroom is
#     if isPalindrome(woord) and len(woord) > 1:
#         palindroom_lijst.append(woord)

# omgekeerd_lijst = []

# for wrd in woordenset:
#     if wrd[::-1] in woordenset and isPalindrome(wrd) == False:
#         omgekeerd_lijst.append(wrd)

# print(f"Het aantal woorden in de lijst is {len(woordenlijst)}")
# print(f"Het langste woord is {langste_woord} en heeft een lengte van {len(langste_woord)} letters")
# print("lijst met palindromen:")
# print(palindroom_lijst)
# print("lijst met omgekeerde woorden (exclusief palindromen)")
# print(omgekeerd_lijst)

# input_woord = input("Voer een woord in: ")
# for wrd in woordenset:
#     if input_woord == wrd:
#         print(f"{input_woord} komt als geheel voor in de lijst!")
#     elif input_woord in wrd:
#         print(f"{input_woord} komt als deel van het woord {wrd} voor!")

        
# from random import randint
# from random import choice


# # Initialisatie
# aantal_dozen = 5
# kat_doos = randint(1,aantal_dozen)
# ronde_nummer = 0
# kat_gevonden = False
# plus_min_tupel = (-1,1)


# # Start van de simulatie
# while not kat_gevonden:
#     doos_te_openen = int(input("Kies een doosnummer: "))
#     ronde_nummer += 1
#     if doos_te_openen == kat_doos:
#         print(f"Raak! Je hebt {ronde_nummer} pogingen nodig gehad")
#         print(f"De kat zat in doos {kat_doos}")
#         kat_gevonden = True
#     else: print("Mis!")

#     if kat_doos == 1:
#         kat_doos = 2
#     elif kat_doos == 5:
#         kat_doos = 4
#     else:
#         kat_doos = kat_doos + choice(plus_min_tupel)