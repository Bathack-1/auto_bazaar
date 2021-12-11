import pyautogui
import keyboard
import time

def kjøpe(gjenstand):

    keyboard.wait("i")
    time.sleep(5)

    #Åpne brazaar
    x, y = pyautogui.position()
    pyautogui.rightClick((x, y))
    print("trykka")
    time.sleep(0.5)

    #Sjekke om du er i bazaar er en spiller
    skjermbilde = pyautogui.screenshot()
    riktig_farge = False
    bazaar_åpnet = False

    while bazaar_åpnet == False:
        for x in range(3392, 3440):
            for y in range(467, 517):

                if skjermbilde.getpixel((x, y)) == (113, 133, 144):
                    riktig_farge = True

        if riktig_farge == False:
            keyboard.press_and_release("esc")
            time.sleep(0.5)
            keyboard.press("space")
            time.sleep(0.3)
            keyboard.release("space")
            print("nope, ikke noe bazaar")
            time.sleep(0.3)
            pyautogui.rightClick()
            skjermbilde = pyautogui.screenshot()

        elif riktig_farge == True:
            bazaar_åpnet = True

    pyautogui.moveTo((3480, 400))
    print("ja, køll")

    if gjenstand == "coal":
        pyautogui.click((3150, 550))
        skjermbilde = pyautogui.screenshot()

def selge():
    pass

def main():
    valg = input("kjøpe eller selge?")
    if valg == "kjøpe":
        kjøpe("coal")
    elif valg == "selge":
        selge()

if __name__ == '__main__':
    main()