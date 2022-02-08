from traceback import format_exc
from main import Telepules

def feladat1(lista):
    print("1)    Hány település található az input fájlban?")
    print(len(lista))
    print()
    
def feladat5(lista):
    print("5)    Hány község rangú település található a Makói kistérségben?")
    kozsegszam = 0
    for t in lista:
        if t.kister == "Makói" and t.rang == "község":
            kozsegszam+=1
    print(kozsegszam)
    print()

def feladat9(lista):
    print("9)    Hány város rangú település található a Szegedi kistérségben?")
    varosszam = 0
    for t in lista:
        if t.kister == "Szegedi" and t.rang == "város":
            varosszam+=1
    print(varosszam)
    print()

def feladat13(lista):
    print("13)    Írja ki a község rangú települések közül az 1000 főnél alacsonyabb népességű települések nevét és népességét!")
    for t in lista:
        if t.rang == "község" and t.nep < 1000:
            print(t.nev + " " + str(t.nep))

def feladat17(lista):
    print("17)    Melyik a legnépesebb település? Írja ki a település nevét és lélekszámát!")
    maxsor = lista[0]
    for t in lista:
        if maxsor.nep < t.nep:
            maxsor.nep = t.nep
            maxsor.nev = t.nev
            
    print(maxsor.nev + " " + str(maxsor.nep))
     
def feladat21(lista):
    print("21)    Melyik a Szentesi kistérség legkisebb területű települése(i)?")
    minsor = lista[0]
    for t in lista:
        if t.kister == "Szentesi" and minsor.ter > t.ter:
            minsor.nev = t.nev
    print(minsor.nev)


"""template

def feladat(lista):
    print('')

    for t in lista:
        if

"""

feladat1(Telepules.lista)

feladat5(Telepules.lista)

feladat9(Telepules.lista)

feladat13(Telepules.lista)

feladat17(Telepules.lista)

feladat21(Telepules.lista)
