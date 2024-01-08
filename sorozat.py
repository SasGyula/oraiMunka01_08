import random

def letrehoz(szam1, szam2):
    print("II/a.")
    print("\t", end="")
    #lista létrehozása
    lista = []
    if szam1 < szam2:
        kisebb = szam1
        nagyobb = szam2
    else:
        kisebb = szam2
        nagyobb = szam1
    for szamom in range(1, 16, 1):
        szam = random.randint(kisebb, nagyobb)
        lista.append(szam)
    #kiirás
    for index in range(0, len(lista),1):
        if index == len(lista)-1:
            print(lista[index], end="")
        else:
            print(f"{lista[index]}", end="%")
    #visszatérési érték
    return lista

def legkisebb(lista):
    print("\nII/b.")
    kiFajl = open("legkisebb.txt", "w", encoding="utf-8")
    print("\tA legkisebb elem:", end="")
    print("\tA legkisebb elem:", end="", file = kiFajl)
    #minimumkereses tétele
    minErtek = lista[0]
    minHely = 0
    index = 1
    while index < len(lista):
        if lista[index] < minErtek:
            minErtek = lista[index]
            minHely = index
        index += 1
    print(f"{minErtek}.")
    print(f"{minErtek}.", file=kiFajl)