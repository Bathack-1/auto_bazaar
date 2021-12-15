import time, keyboard, pyautogui


def start():
    keyboard.wait("i")
    time.sleep(5)


#flytte bort datamusa, og vente
def bort(x=4120, y=400, vente_tid=0.2):
    pyautogui.moveTo((x, y))
    time.sleep(vente_tid)


def trykk(posisjon_x, posisjon_y=570):
    global skjermbilde

    bort()
    skjermbilde = pyautogui.screenshot()
    pyautogui.click(posisjon_x, posisjon_y)
    time.sleep(0.2)


def åpne_bazaar():

    #Åpne brazaar og sjekke om du er i bazaar elelr er en i spiller
    riktig_farge = False
    bazaar_åpnet = False

    while not bazaar_åpnet:

        pyautogui.rightClick()
        time.sleep(1)
        pyautogui.moveTo(4075, 480)
        skjermbilde = pyautogui.screenshot()
        #time.sleep(0.5)

        if skjermbilde.getpixel((4058, 478)) == (184, 194, 200) :
            riktig_farge = True

        if riktig_farge == False:
            keyboard.press_and_release("esc")
            time.sleep(0.5)
            keyboard.press("space")
            time.sleep(0.3)
            keyboard.release("space")
            time.sleep(0.2)

        elif riktig_farge is True:
            bazaar_åpnet = True

    time.sleep(1)

def tilgjenglig(kjøpe_eller_selge):
    sjekke_x = 0
    sjekke_y = 0
    farge = (0, 0, 0)
    if kjøpe_eller_selge == "kjøpe":
        sjekke_x = 3735
        sjekke_y = 560
        farge = (146, 60, 49)

    elif kjøpe_eller_selge == "selge":
        sjekke_x = 3840
        sjekke_y = 560
        farge = (145, 63, 48)

    skjermbilde = pyautogui.screenshot()
    if skjermbilde.getpixel((sjekke_x, sjekke_y)) == farge:
        svar = False
    else:
        svar = True
    return svar


def hente_inn(kjøp_eller_selge, vente_før_begynne):

    time.sleep(vente_før_begynne)
    noe_der = True
    x = 0
    y = 0

    åpne_bazaar()
    trykk(3900, 715)
    bort()
    if kjøp_eller_selge == "kjøpe":
        x = 3678
        y = 626
    elif kjøp_eller_selge == "selge":
        x = 3680
        y = 570

    while noe_der == True:
        skjermbilde = pyautogui.screenshot()
        if skjermbilde.getpixel((x, y)) == (139, 139, 139) or skjermbilde.getpixel((x, y)) == (197, 197, 197):
            break

        if noe_der == True:
            trykk(x, y)

        if tilgjenglig("kjøpe") == False or tilgjenglig("selge") == False:
            noe_der = False

            if kjøp_eller_selge == "selge":
                trykk(3840, 560)
                keyboard.press_and_release("esc")
                åpne_bazaar()
                trykk(3900, 700)
                skjermbilde = pyautogui.screenshot()
                if skjermbilde.getpixel((3732, 950)) != (139, 139, 139):
                    trykk(3732, 950)
                    trykk(4000)
                    trykk(3790)
                    trykk(3840)
                    hente_inn("selge", vente_før_begynne)
            else:
                trykk(3735, 560)
                keyboard.press_and_release("esc")
                hente_inn(kjøp_eller_selge, vente_før_begynne)
