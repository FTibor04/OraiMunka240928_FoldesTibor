def elso():
    print("A program eldönti egy egész számról, hogy pozitív-e!")
    szam=int(input("Kérem adjon meg egy számot!: "))

    if szam>0:
        print("A szám pozitív")
    else:
        print("A szám negatív")

def masodik():
    print("A program eldönti egy egész számról, hogy pozitív-e!")
    szam = int(input("Kérem adjon meg egy számot!: "))

    if (szam >= -9) and (szam<=9):
        megelozo = szam - 1
        rakoveto = szam + 1
        print("A rákövetkező érték: "+str(rakoveto)+", a megelőző érték: "+str(megelozo))
