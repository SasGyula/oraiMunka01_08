def hossz():
        szo1 = input("\t Kérek egy szót!")
        szo2 = input("\t Kérek egy másik szót!")
        if len(szo1) > len(szo2):
            nagyobb = szo1
            szavakHossza = len(szo1) - len(szo2)
        elif len(szo1) < len(szo2):
            nagyobb = szo2
            szavakHossza = len(szo2) - len(szo1)
        elif len(szo1) == len(szo2):
            nagyobb = "egyenlő!"
            szavakHossza = 0

        print(f"A hosszab szó: {nagyobb}")
        if len(szo1) != len(szo2):
            print(f"\t A szavak hosszának különbsége: {szavakHossza}")
