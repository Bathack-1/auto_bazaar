from felles_funksjoner import *

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

    if gjenstand == "coal":
        #objekt_farge = (45, 45, 45)

        trykk(3790, 550)
        trykk(3680)
        kjøp_og_bekreft(antall)
        hente_inn("kjøpe", 5)