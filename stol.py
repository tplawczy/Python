

class Program():
    def __init__(self):
        self.deski = []
        self.e = 0
        self.n = 0
        self.d = 0


    def wczytywanie_liczby(self):
        a = " "
        print('Podaj liczbę:' + a)
        a = input()
        return int(a)

    def wprowadzanie_liczb(self, a):
        self.n = self.wczytywanie_liczby()
        for i in range(0,self.n):
            a.append(self.wczytywanie_liczby())
        self.d = self.wczytywanie_liczby()

    def wyszukiwanie_liniowe(self, deski, n, d):

        j = 0
        for i in range(0, n):
            if (deski[i] >= d):
                j += 1

        print('Liczba desek nadających się na blat: ' + str(j))




# Press the green button in the gutter to run the script.



if __name__ == '__main__':
    o = Program()
    o.wprowadzanie_liczb(o.deski)
    o.wyszukiwanie_liniowe(o.deski,o.n,o.d)




