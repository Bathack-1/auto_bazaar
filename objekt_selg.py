from felles_funksjoner import *

def objekt_selg():
    start()
    åpne_bazaar()
    trykk(3260,700)
    skjermbilde = pyautogui.screenshot()
    if skjermbilde.getpixel((3092, 974)) != (139, 139, 139):
        trykk(3092, 974)

    trykk(3360)
    trykk(3150)
    trykk(3200)
    hente_inn("selge", 30)
