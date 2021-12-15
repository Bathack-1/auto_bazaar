from felles_funksjoner import *
from objekt_liste import objekt_liste

def kjøp_og_bekreft(antall):
    # trykke kjøp
    trykk(3950)

    # velge antall
    trykk(4000)

    time.sleep(0.2)
    keyboard.write(str(antall), 0.1)
    trykk(3850, 750)

    # bekrefte kjøp
    trykk(3790)
    trykk(3840)

def objekt_kjøp(gjenstand, antall):

    åpne_bazaar()
    objekt_liste(gjenstand)
    kjøp_og_bekreft(antall)

    vente_før_begynne = objekt_liste(gjenstand)
    hente_inn("kjøpe", vente_før_begynne)