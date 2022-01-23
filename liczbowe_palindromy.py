
class Program():
    def __init__(self):
        self.n = 0
        self.s = Liczba()
        self.v = 0

    def wczytywanie_liczby(self):
        a = " "
        print('Podaj liczbę:' + a)
        a = input()
        return int(a)

    def wprowadzanie_liczb(self):
        self.n = self.wczytywanie_liczby()

        for i in range(0,self.n):
            self.s.z.append(str(self.wczytywanie_liczby()))


    def czy_jest_palindromem(self, s):
        return s == s[::-1]

class Liczba():
    def __init__(self):
        self.z = []





# Press the green button in the gutter to run the script.



if __name__ == '__main__':
    o = Program()
    o.wprowadzanie_liczb()
    for i in range (0,o.n):
        if o.czy_jest_palindromem(o.s.z[i]):
            print(o.s.z[i])
            o.v = 1
    if o.v == 0:
        print ("Brak")




