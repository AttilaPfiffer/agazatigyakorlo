def feladat1():
    muzeum_neve: str = (input("Adja meg a múzeum nevét: "))
    latogato: str = (input("Látogató neve: "))

    ertekeles: int = (input("Adja meg az értékelést (1 - 20): "))

    if 1 <= ertekeles <= 20:
        print("Köszönjük az értékelést!")
    elif ertekeles > 20: 
        print("20 pont feletti értékelés nem elfogadható!")
    elif ertekeles <= 0:
        print("Az értékelés nem lehet negatív vagy 0!")