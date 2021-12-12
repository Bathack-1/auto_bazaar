from felles_funksjoner import *

def kjøp_og_bekreft(antall):
    # trykke kjøp
    trykk(3310)

    # velge antall
    trykk(3360)

    time.sleep(0.2)
    keyboard.write(str(antall), 0.1)
    trykk(3210, 750)

    # bekrefte kjøp
    trykk(3150)
    trykk(3200)

def objekt_kjøp(gjenstand, antall):
    start()
    åpne_bazaar()

    if gjenstand == "coal":
        #objekt_farge = (45, 45, 45)

        trykk(3150, 550)
        trykk(3040)
        kjøp_og_bekreft(antall)
        hente_inn("kjøpe", 5)