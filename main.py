from objekt_kjøp import objekt_kjøp

def kjøpe(gjenstand, antall=71680):
    objekt_kjøp(gjenstand, antall)


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