# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Program():

    def text(self):
        self.x=""
        print('Podaj wiadomosc ' + self.x)
        self.x = input()
    def szyfruj(self, z):
            w = z.replace("a","1")
            w1 = w.replace("e", "2")
            w2 = w1.replace("i","3")
            w3=w2.replace("o","4")
            w4 = w3.replace("u", "5")
            w5 = w4.replace("y", "6")
            self.x = w5
            return w5
    def deszyfruj(self, z):
           w = z.replace("1", "a")
           w1 = w.replace("2", "e")
           w2 = w1.replace("3", "i")
           w3 = w2.replace("4", "o")
           w4 = w3.replace("5", "u")
           w5 = w4.replace("6", "y")
           self.x =w5
           return w5
def szyfr():
    a = Program()
    a.text()
    print("Wykonuję funkcję szyfruj na tekście: "+a.x)
    a.szyfruj(a.x)
    print("Po wykonaniu szyfrowania: " + a.x)

    print("Wykonuję funkcję deszyfruj na tekście: "+ a.x)
    a.deszyfruj(a.x)
    print("Po wykonaniu deszyfrowania: " + a.x)




if __name__ == "__main__":
    szyfr()

