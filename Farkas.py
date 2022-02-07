from main import Telepules

def feladat4(lista):
    print("4)    Van-e falu rangú település?")
    print("Igen, van" if len(list(filter(lambda t: t.rang == "falu", lista)))>0 else "Nincsen!")
    print()

def feladat8(lista):
    print("8)    Hány város rangú település található a Makói kistérségben?")
    print(len(list(filter(lambda t: t.kister == "Makói" and t.rang == "város", lista))))
    print()

def feladat12(lista):
    print("12)    Írja ki a város rangú települések közül az 10000 főnél népesebb települések nevét és népességét!")
    a = list(filter(lambda t: t.rang == "város" and t.nep > 1000, lista))
    for sor in a:
        print(f"{sor.nev} {str(sor.nep)}")
    print()

def feladat16(lista):
    print("16)    Mennyi a legalacsonyabb népességű település lélekszáma?")
    print(list(filter(lambda t: t.nep == min(map(lambda t: t.nep, lista)), lista))[0].nev)
    print()

def feladat20(lista):
    print("20)    Melyik a Szegedi kistérség legkisebb területű települése(i)?")
    print()

def feladat24(lista):
    print("24)    Melyik a Szentesi kistérség legnépesebb települése(i)?")
    print()

def feladat28(lista):
    print("28)    Írja ki a Kisteleki kistérség településeinek népsűrűségét!")
    print()

def feladat32(lista):
    print("32)    Igaz-e, hogy minden Kisteleki kistérségű település lélekszáma kisebb, mint 10000?")
    print()

def feladat36(lista):
    print("36)    Írja ki a Kisteleki kistérség településeinek egy lakásra jutó népesség számát!")
    print()

def feladat40(lista):
    print("40)    Készítsen kimutatást kistérségi bontásban, amelyben megadja az egyes kistérségek összterületének a nagyságát!")
    print()




feladat4(Telepules.lista)
feladat8(Telepules.lista)
feladat12(Telepules.lista)
feladat16(Telepules.lista)
feladat20(Telepules.lista)
feladat24(Telepules.lista)
feladat28(Telepules.lista)
feladat32(Telepules.lista)
feladat36(Telepules.lista)
feladat40(Telepules.lista)