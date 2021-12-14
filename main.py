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

    valg = input("kjøpe eller selge?")
    if valg == "kjøpe":
        def jobb(gjenstand):
            kjøpe(gjenstand)
    elif valg == "selge":
        def jobb():
            selge()
    elif valg == "begge":
        def jobb(gjenstand):
            kjøpe(gjenstand)
            selge()

    valg = input("\n"+"antall ganger?")

    if valg == "for alltid":
        antall_rep = 0
        while not keyboard.is_pressed("å"):
            start()
            while True:
                jobb("coal")
                antall_rep += 1
                print(f"{antall_rep} \n")
    else:
        antall_rep = 0
        while not keyboard.is_pressed("å"):
            start()
            for x in range(int(valg)):
                jobb("coal")
                antall_rep += 1
                print(f"{antall_rep} \n")

if __name__ == '__main__':
    main()