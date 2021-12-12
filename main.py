import keyboard

from objekt_kjøp import objekt_kjøp
from objekt_selg import objekt_selg

def kjøpe(gjenstand, antall=71680):
    objekt_kjøp(gjenstand, antall)


def selge():
    objekt_selg()

def main():
    while not keyboard.is_pressed("å"):
        valg = input("kjøpe eller selge?")
        if valg == "kjøpe":
            kjøpe("coal")
        elif valg == "selge":
            selge()

if __name__ == '__main__':
    main()