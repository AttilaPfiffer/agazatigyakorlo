import random

def feladat2():
    veletlen_szam = []
    for i in range(8):
        szam: int = random.randint(-90, 500)
        veletlen_szam.append(str(szam))
        if i < 7:
            print(szam, end = ";")
        else:
            print(szam, end = "")

def feladat3(veletlen_szam):
    szamlalo = []
    for i in range(0, len(veletlen_szam), 1):
        if veletlen_szam[i] % 10 == 0:
            szamlalo += 1
        i += 1
    return szamlalo