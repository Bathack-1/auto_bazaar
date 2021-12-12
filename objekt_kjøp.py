from felles_funksjoner import *

def kjøp_og_bekreft(antall):
    # trykke kjøp
    trykk(3310)

    # velge antall
    trykk(3360)

    time.sleep(0.2)
    keyboard.write(str(antall), 0.1)

    # bekrefte kjøp
    trykk(3210, 750)
    trykk(3140)
    trykk(3200)

def hente_inn(vente_før_begynne):
    time.sleep(vente_før_begynne)
    noe_der = True

    åpne_bazaar()
    trykk(3260, 715)
    bort()

    while noe_der == True:
        skjermbilde = pyautogui.screenshot()
        if skjermbilde.getpixel((3038, 626)) == (139, 139, 139):
            noe_der = False

        if noe_der == True:
            trykk(3030, 625)

        elif noe_der == False:
            exit()

        if tilgjenglig("kjøpe") == False:
            noe_der = False
            keyboard.press_and_release("esc")
            hente_inn(vente_før_begynne)

def objekt_kjøp(gjenstand, antall):
    start()
    åpne_bazaar()

    if gjenstand == "coal":
        #objekt_farge = (45, 45, 45)

        trykk(3150, 550)
        trykk(3040)
        kjøp_og_bekreft(antall)
        hente_inn(5)