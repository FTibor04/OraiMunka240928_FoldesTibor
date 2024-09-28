import random
def tizenegyedikFeladat():
    szam1=random.randint(50,100)
    szam2=random.randint(50,100)

    print("szam1"+str(szam1)+", szam2"+str(szam2))
    atmeneti = szam1
    szam1 = szam2
    szam2 = atmeneti

    print("szam1"+str(szam1)+", szam2"+str(szam2))
