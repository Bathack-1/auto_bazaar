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

    kjøpe_eller_selge = input("kjøpe eller selge? ")
    if kjøpe_eller_selge == "kjøpe":
        def jobb(gjenstand):
            kjøpe(gjenstand)
    elif kjøpe_eller_selge == "selge":
        def jobb():
            selge()
    elif kjøpe_eller_selge == "begge":
        def jobb(gjenstand):
            kjøpe(gjenstand)
            selge()

    if kjøpe_eller_selge == "kjøpe" or kjøpe_eller_selge == "begge":
        kjøpes = input("\n"+"hva skal kjøpes? ")
    else:
        kjøpes = False

    valg = input("\n"+"antall ganger? ")

    if valg == "for alltid":
        antall_rep = 0
        while not keyboard.is_pressed("å"):
            start()
            while True:
                jobb(kjøpes)
                antall_rep += 1
                print(f"{antall_rep} \n")
    else:
        antall_rep = 0
        while not keyboard.is_pressed("å"):
            start()
            for x in range(int(valg)):
                jobb(kjøpes)
                antall_rep += 1
                print(f"{antall_rep} \n")

if __name__ == '__main__':
    main()