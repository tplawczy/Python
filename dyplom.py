# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




import numpy as array



class Network:
    def __init__(self):

        self.nodes=array.zeros((9, 6),dtype=int )





    def wypisz(self, file):
        plik = open(file).read()
        print(plik)

    def wczytaj(self, file):
        with open(file, "r") as f:
            list = [line.rstrip("\n") for line in f]
            print(list)
            for i in range(0,len(list)):
                for j in range(0,len(list[i-1])):
                    var=list[i-1]
                    self.nodes[i-1][j-1] = int(var[j-1])
        print(type(self.nodes))
        print(self.nodes)









class Individual:
    def __init__(self, Network):
        self.genom = []


    def generate(self, genom):
        genom.append(1)
        



class Population:
    def __init__(self):
        var='rty'


def dyplom():
    file = 'plik.txt'
    c=Network()
    c.wczytaj(file)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
