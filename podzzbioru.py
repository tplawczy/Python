
from copy import deepcopy
class Podzbior():
    def __init__(self, n, j, k):
        self.n = n
        self.j = n
        self.BLOK = []
        self.PR = []
        self.k = k
        self.NAST = []
        self.POPRZ = []

    def getIndexNast(selfself, x):
        for i in range(1, len(self.BLOK)):
            if self.BLOK[i] == x:
                z = i + 1
                return z

    def getNast(self, x):
        if self.getIndexNast(x) < len(self.BLOK):
            return z + 1
        return 0

    def getIndexPoprz(self, x):
        for i in range(self.BLOK, 1, -1):
            if self.BLOK[i] == x:
                z = i - 1
                return z

    def getPoprz(self, x):
        if self.getIndexNast(x) > 0:
            return z - 1
        return 0

    def setNast(self, x, v):
        self.BLOK[self.getIndexNast(x) - 1] = v

    def setPoprz(self, x, v):
        self.BLOK[self.getPoprz(x) + 1] = v


class Generator():

    def __init__(self, Podzbior):
        self.Podzbior = Podzbior

    def generuj(self, Podzbior):
        for i in range(0, self.Podzbior.n):
            self.Podzbior.BLOK.append(1)
            self.Podzbior.PR.append(True)
            self.Podzbior.NAST.append(0)
            self.Podzbior.POPRZ.append(0)

        self.Podzbior.NAST[0] = 0
        print(self.Podzbior.BLOK)
        while self.Podzbior.j > 1:
            self.Podzbior.k = self.Podzbior.BLOK[self.Podzbior.j - 1]
            if self.Podzbior.PR[self.Podzbior.j - 1]:
                if self.Podzbior.NAST[self.Podzbior.k - 1] == 0:
                    self.Podzbior.NAST[self.Podzbior.k - 1] = self.Podzbior.j
                    self.Podzbior.POPRZ[self.Podzbior.j - 1] = self.Podzbior.k
                    self.Podzbior.NAST[self.Podzbior.j - 1] = 0
                if self.Podzbior.NAST[self.Podzbior.k - 1] > self.Podzbior.j:
                    self.Podzbior.POPRZ[self.Podzbior.j - 1] = self.Podzbior.k
                    self.Podzbior.NAST[self.Podzbior.j - 1] = self.Podzbior.NAST[self.Podzbior.k - 1]
                    self.Podzbior.POPRZ[self.Podzbior.NAST[self.Podzbior.j - 1] - 1] = self.Podzbior.j
                    self.Podzbior.NAST[self.Podzbior.k - 1] = self.Podzbior.j
                self.Podzbior.BLOK[self.Podzbior.j - 1] = self.Podzbior.NAST[self.Podzbior.k - 1]

            else:
                self.Podzbior.BLOK[self.Podzbior.j - 1] = self.Podzbior.POPRZ[self.Podzbior.k - 1]
                if self.Podzbior.k == self.Podzbior.j:
                    if self.Podzbior.NAST[self.Podzbior.k - 1] == 0:
                        self.Podzbior.NAST[self.Podzbior.POPRZ[self.Podzbior.k - 1] - 1]
                    else:
                        self.Podzbior.NAST[self.Podzbior.POPRZ[self.Podzbior.k - 1] - 1] = 0
                        self.Podzbior.POPRZ[self.Podzbior.NAST[self.Podzbior.k - 1] - 1] = self.Podzbior.POPRZ[
                            self.Podzbior.k - 1]
            list1 = []
            for i in range(1, len(self.Podzbior.BLOK) + 1):

                list = []

                for l in range(1, len(self.Podzbior.BLOK) + 1):

                    if self.Podzbior.BLOK[l - 1] == i:

                        list.append(l)

                list1+=deepcopy(list)
                print(list1)
            self.Podzbior.j = self.Podzbior.n
            while (self.Podzbior.j > 1) and ((self.Podzbior.PR[self.Podzbior.j - 1] and self.Podzbior.BLOK[
                self.Podzbior.j - 1] == self.Podzbior.j) or (
                                                     not self.Podzbior.PR[self.Podzbior.j - 1] and self.Podzbior.BLOK[
                                                 self.Podzbior.j - 1] == 1)):
                self.Podzbior.PR[self.Podzbior.j - 1] = not self.Podzbior.PR[self.Podzbior.j - 1]
                self.Podzbior.j = self.Podzbior.j - 1


def zbiory():
    pz = Podzbior(5, 5, 5)

    g = Generator(pz)
    g.generuj(Podzbior)


if __name__ == "__main__":
    zbiory()
