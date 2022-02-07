class Telepules:
    lista = []
    def __init__(self, azon, nev, rang, kister, ter, nep, lakasok):
        self.azon = azon
        self.nev = nev
        self.rang = rang
        self.kister = kister
        self.ter = ter
        self.nep = nep
        self.lakasok = lakasok
        Telepules.lista.append(self)





with open("J.txt", "r", encoding="utf8") as f:

    for sor in f:
        s = sor.strip().split(";")
        t = Telepules(s[0], s[1], s[2], s[3], int(s[4]), int(s[5]), int(s[6]))

