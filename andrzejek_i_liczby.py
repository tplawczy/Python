# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class liczba():

    def __init__(self):

        self.rosnaca = 0
        self.malejaca = 0
        self.max=0
        self.rozn=0

    def roznica(self, n):
        lista =[]
        napis = str(n)
        napis1=""
        napis2=""
        suma = 0
        for znak in napis:
            cyfra = int(znak)
            lista.append(cyfra)

        lista.sort()
        for x in lista:
            napis1 += str(x)
        self.rosnaca = int(napis1)
        lista.sort(reverse=True)

        for x in lista:
            napis2 += str(x)
        self.malejaca = int(napis2)
        self.rozn = self.malejaca - self.rosnaca
        return self.rozn

def roznice():
    g = 1000000000
    a = liczba()

    for x in range(g,0,-1):
        print(a.roznica(x))
        if a.max < a.roznica(x):
            a.max = a.roznica(x)



    print('------------')
    print(a.max)

if __name__ == "__main__":
    roznice()

