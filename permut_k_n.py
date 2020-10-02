
class Zbior():
    def __init__(self, n, k):
        self.n = n
        self.elementy = []
        self.k = k
        self.p = self.k

    def wypelnij(self):
        for i in range(1, self.k+1):
            self.elementy.append(i)

    def wyswietl(self):
        print(self.elementy)



class Generator():
    def __init__(self, Zbior):
        self.Zbior = Zbior
    def generuj(self):

        while self.Zbior.p >= 1:
            self.wyswietl()
            if self.Zbior.elementy[self.Zbior.k-1] == self.Zbior.n:
                self.Zbior.p = self.Zbior.p - 1
            else:
                self.Zbior.p = self.Zbior.k
            if  self.Zbior.p >= 1:
                for i in range (self.Zbior.k, self.Zbior.p-1, -1):
                    self.Zbior.elementy[i-1] = self.Zbior.elementy[self.Zbior.p-1] + i - self.Zbior.p + 1
    def wyswietl(self):
        
                print (self.Zbior.elementy)
def main():
    zb=Zbior(5,3)
    zb.wypelnij()
    g=Generator(zb)
    g.generuj()

