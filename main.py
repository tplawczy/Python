# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



class Lista():
    i = 0
    p = 0
    j = 0

    def __new__(self, n):
        self.n = n
        list = []
        for i in range(1, self.n):
            list.append(0)
        return Lista

    def __init__(self, n):
        self.n = n
        Lista(n)


class Zbiory:


    def __init__(self, Lista):
        self.Lista = Lista

    def wygenerujKolejny(self):
        while Lista.p < Lista.n:
            Lista.i += 1
            Lista.p = 1
            Lista.j = Lista.i
            while Lista.j % 2 == 0:
                Lista.j = j / 2
                Lista.p += 1
            if Lista.p <= Lista.n:

                if Lista[(Lista.p) - 1] == 0:
                    Lista[(Lista.p) - 1] = 1
                else:
                    Lista[(Lista.p) - 1] = 0

            print(Lista)


def main():
    l = Lista(4)
    e = Zbiory(l)
    print(Lista[Lista.p])
    e.wygenerujKolejny()


if __name__ == "__main__":
    main()

