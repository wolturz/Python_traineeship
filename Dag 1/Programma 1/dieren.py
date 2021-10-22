# Het programma begint met een basisset aan dieren
# De gebruikte datastructuur is een Python dictionary
import pickle

bestandsnaam = 'dieren_kiezen.txt'
alle_dieren_bestand = 'alle_dieren.txt'

modus = 'rt'


try:
    f = open(alle_dieren_bestand,modus)
    alle_dieren_pickled = eval(f.read())
    alle_dieren = pickle.loads(alle_dieren_pickled)
    f.close()
except:
    alle_dieren = ['rups', 'huismus', 'olifant']

try:
    f = open(bestandsnaam,modus)
    dieren_pickled = eval(f.read())
##    print(f"This is my pickled object: \n{dieren_pickled}\n")
    dieren = pickle.loads(dieren_pickled)
    f.close()
except:
    dieren = {
        'vraag': 'Heeft het dier 4 poten?',
        'nee': {
            'vraag': 'Kruipt het op bladeren?',
            'ja':'rups',
            'nee':'huismus'
        },
        'ja': 'olifant'
    }



# Herhalen zolang de gebruiker dat wil
def raad_het_dier(alle_dieren):
    print('Neem een dier in gedachten...')
    prompt = 'Ben je er klaar voor?'
    while vraag_ja_nee(prompt):
        alle_dieren = doorloop_dieren_boomstructuur(dieren, alle_dieren)
        print("Wil je nu alle dieren zien?")
        if input() == 'ja':
             print(alle_dieren)        
        prompt = 'Wil je nog een keer spelen?'
# Doorloop een tak
def doorloop_dieren_boomstructuur(tak, alle_dieren):
    # We stellen eerst de vraag die op de tak beschikbaar is
    # De vraag heeft het formaat ['is'|'heeft'] het dier 'eigenschap'
    richting = vraag_ja_nee(tak['vraag'].capitalize() + '?')
    nieuwe_tak = lagere_tak(tak, richting)

    if dier_gevonden(nieuwe_tak):
        alle_dieren = eindig_spel(nieuwe_tak, tak, richting,alle_dieren)
    else:
        doorloop_dieren_boomstructuur(nieuwe_tak, alle_dieren)
    return alle_dieren

# Een dier is gevonden als de tak waarop we zitten eindigt in een blad,
# in plaats van in een lagere tak. Een blad is een string, een
# lagere tak is een dict. We controleren op een blad met de functie
# isinstance
def dier_gevonden(tak):
    is_blad = not isinstance(tak, dict)
    return is_blad

def eindig_spel(blad, stam, richting, alle_dieren):
    if vraag_ja_nee('Is je dier misschien een ' + blad + '?'):
        print('Yes! Ik het het geraden! Ik ben zo goed!')
    else:
        alle_dieren = bewaar_nieuw_dier(stam, welke_kant(richting), blad,alle_dieren)
    return alle_dieren

def bewaar_nieuw_dier(hogere_tak, kant, oud_dier,alle_dieren):
    nieuw_dier = input('Oh, wat jammer dat ik het niet heb geraden! Welk dier zat je aan te denken? ')
    if nieuw_dier.startswith('een '):
        nieuw_dier = nieuw_dier[4:len(nieuw_dier)]
    alle_dieren.append(nieuw_dier)
    nieuwe_vraag = input('En welke vraag had ik moeten stellen om onderscheid te maken tussen een ' + oud_dier.lower() + ' en een ' + nieuw_dier.lower() + '? ')

    hogere_tak[kant] = {
        'vraag': nieuwe_vraag.lower().rstrip('? ').lstrip(' ').replace('  ', ' '),
        'ja': nieuw_dier.lower(),
        'nee': oud_dier
    }
    return alle_dieren
       

# Geef een deel van de boomstructuur terug die begint met
# ja of nee
def lagere_tak(tak, richting):
    if richting:
        return tak['ja']
    else:
        return tak['nee']

def welke_kant(ja):
    if ja:
        return 'ja'
    else:
        return 'nee'

def vraag_ja_nee(vraag):
    antwoord = input(vraag + ' ')
    return is_ja(antwoord)

def is_ja(tekst):
    if tekst.lower().startswith('j'):
        return True
    else:
        return False

raad_het_dier(alle_dieren)

dieren_pickled = pickle.dumps(dieren)
alle_dieren_pickled = pickle.dumps(alle_dieren)

modus = 'at' # aanmaken, create, tekstbestand
f = open(bestandsnaam, modus)
f.write(str(dieren_pickled))
f.close() # sluit het bestand

f = open(alle_dieren_bestand, modus)
f.write(str(alle_dieren_pickled))
f.close()
