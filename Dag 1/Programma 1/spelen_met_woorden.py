bestandsnaam = "woorden.txt"
modus = 'rt'
woordenbestand = open(bestandsnaam,modus)
woordenlijst = woordenbestand.read().splitlines()       # splitlines haalt '\n' wel weg, readlines() niet
woordenset = set(woordenlijst)

def isPalindrome(s):
    return s == s[::-1]

langste_woord = ''
for woord in woordenlijst:              # elke lengte van het woord vergelijken of het langer is, zo ja, dan is dit het nieuwe langste woord
    if len(woord) > len(langste_woord):
        langste_woord = woord

palindroom_lijst = []

for woord in woordenlijst:              # opzoeken of een woord een palindroom is
    if isPalindrome(woord) and len(woord) > 1:
        palindroom_lijst.append(woord)

omgekeerd_lijst = []

for wrd in woordenset:
    if wrd[::-1] in woordenset and isPalindrome(wrd) == False:
        omgekeerd_lijst.append(wrd)

print(f"Het aantal woorden in de lijst is {len(woordenlijst)}")
print(f"Het langste woord is {langste_woord} en heeft een lengte van {len(langste_woord)} letters")
print("lijst met palindromen:")
print(palindroom_lijst)
print("lijst met omgekeerde woorden (exclusief palindromen)")
print(omgekeerd_lijst)

input_woord = input("Voer een woord in: ")
for wrd in woordenset:
    if input_woord == wrd:
        print(f"{input_woord} komt als geheel voor in de lijst!")
    elif input_woord in wrd:
        print(f"{input_woord} komt als deel van het woord {wrd} voor!")