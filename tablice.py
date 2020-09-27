# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




class Lista:
    i=0
    p=0
    j=0
    def __new__(self, n):
        self.n=n
        list = []
        for i in range(1,n):
            list.append(0)
            return list


class Zbiory:
    Lista
    def __init__(self, Lista):
        self.Lista = Lista

    def wygenerujKolejny(self):
        while Lista.p > Lista.n:
            Lista.i += 1
            Lista.p = 1
            Lista.j = Lista.i
            while Lista.j % 2 == 0:
                    Lista.j = j / 2
                    Lista.p += 1
            if Lista.p <= Lista.n:
                Lista[Lista.p] = 1 - Lista[Lista.p]
            print(Lista)















def main():
    l = Lista(4)
    e=Zbiory(l)
    e.wygenerujKolejny()




if __name__ == "__main__":
    main()
