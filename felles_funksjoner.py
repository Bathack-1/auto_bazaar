import time, keyboard, pyautogui

def start():
    keyboard.wait("i")
    time.sleep(5)


#flytte bort datamusa, og vente
def bort(x=3480, y=400, vente_tid=0.2):
    pyautogui.moveTo((x, y))
    time.sleep(vente_tid)


def trykk(posisjon_x, posisjon_y=570):
    global skjermbilde

    bort()
    skjermbilde = pyautogui.screenshot()
    pyautogui.click(posisjon_x, posisjon_y)


def åpne_bazaar():

    #Åpne brazaar og sjekke om du er i bazaar elelr er en i spiller
    riktig_farge = False
    bazaar_åpnet = False

    while bazaar_åpnet == False:

        pyautogui.rightClick()
        skjermbilde = pyautogui.screenshot()
        time.sleep(0.5)

        if skjermbilde.getpixel((3416, 491)) == (113, 133, 144):
            riktig_farge = True

        if riktig_farge == False:
            keyboard.press_and_release("esc")
            time.sleep(0.5)
            keyboard.press("space")
            time.sleep(0.3)
            keyboard.release("space")
            time.sleep(0.2)

        elif riktig_farge == True:
            bazaar_åpnet = True

def tilgjenglig(kjøpe_eller_selge):
    svar = True
    sjekke_x = 0
    sjekke_y = 0
    farge = (0, 0, 0)
    if kjøpe_eller_selge == "kjøpe":
        sjekke_x = 3095
        sjekke_y = 560
        farge = (146, 60, 49)

    if kjøpe_eller_selge == "selge":
        pass
    skjermbilde = pyautogui.screenshot()
    if skjermbilde.getpixel((sjekke_x, sjekke_y)) == farge:
        svar = False
    else:
        svar = True
    return svar