from felles_funksjoner import *

def objekt_selg():
    åpne_bazaar()
    trykk(3900,700)
    skjermbilde = pyautogui.screenshot()
    if skjermbilde.getpixel((3092, 974)) != (139, 139, 139):
        trykk(3732, 974)

    trykk(4000)
    trykk(3790)
    trykk(3840)
    hente_inn("selge", 30)
