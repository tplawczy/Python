# This is a sample Python script.
# Binarny kod greya
class Lista():
    i =0
    p =0
    j =0
    list=[]

    def __new__(self, n):
        self.n = n
        for i in range(1, self.n+1):
            self.list.append(0)
        return Lista

    def __init__(self, n):
        self.n = n
        Lista(n)

class Zbiory:
    Lista

    def __init__(self, Lista):
        self.Lista = Lista

    def wygenerujKolejny(self, Lista):
        while Lista.p <= Lista.n:
            print(Lista.list)
            Lista.i += 1
            Lista.p = 1
            Lista.j = Lista.i
            while Lista.j % 2 == 0:
                Lista.j = Lista.j / 2
                Lista.p = Lista.p + 1
            if Lista.p <= Lista.n:

                if Lista.list[(Lista.p)-1] == 0:
                    Lista.list[(Lista.p)-1] = 1
                else:
                    Lista.list[(Lista.p)-1] = 0




def main():
    l = Lista(4)
    e = Zbiory(l)
    e.wygenerujKolejny(l)


if __name__ == "__main__":
    main() 
