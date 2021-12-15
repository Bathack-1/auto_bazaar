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
    vente_tid = objekt_liste(gjenstand)    #kjører "objekt_liste", og lagrer det den returnerer i vente_tid
    kjøp_og_bekreft(antall)
    hente_inn("kjøpe", vente_tid)