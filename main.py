import keyboard

from objekt_kjøp import objekt_kjøp
from objekt_selg import objekt_selg
from felles_funksjoner import start

def kjøpe(gjenstand, antall=71680):
    objekt_kjøp(gjenstand, antall)


def selge():
    objekt_selg()


def main():
    global jobb

    kjøpe_eller_selge = input("kjøpe eller selge? ").lower()
    if kjøpe_eller_selge == "kjøpe":
        def jobb(gjenstand, antall):
            kjøpe(gjenstand, antall)
    elif kjøpe_eller_selge == "selge":
        def jobb():
            selge()
    elif kjøpe_eller_selge == "begge":
        def jobb(gjenstand, antall):
            kjøpe(gjenstand, antall)
            selge()

    if kjøpe_eller_selge == "kjøpe" or kjøpe_eller_selge == "begge":
        kjøpes = input("\n"+"Hva skal kjøpes? ").lower()
        antall = input("\n"+"Hvor mye skal kjøpes?")
        if antall == "" or antall == " ":
            antall = 71680
    else:
        kjøpes = False
        antall = False

    valg = input("\n"+"antall ganger? ").lower()

    if valg == "for alltid":
        antall_rep = 0
        while not keyboard.is_pressed("å"):
            start()
            while True:
                jobb(kjøpes, antall)
                antall_rep += 1
                print(f"{antall_rep} \n")
    else:
        antall_rep = 0
        while not keyboard.is_pressed("å"):
            start()
            for x in range(int(valg)):
                jobb(kjøpes, antall)
                antall_rep += 1
                print(f"{antall_rep} \n")

if __name__ == '__main__':
    main()