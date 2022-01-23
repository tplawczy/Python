# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Program():

    def wiadomosc(self):
        x=""
        y=""
        z=""

        print('Podaj imię ' + x)
        x = input()
        print('Podaj Nazwisko '+ y )
        y = input()
        print('Podaj wiek ' + z)
        z = input()

        for v in range(1,20):
            print('Witaj '+ x +' '+ y +'. Skończysz 100 lat w roku '+str(2020+(100-int(z))))

def wiek():
    a = Program()
    a.wiadomosc()

if __name__ == "__main__":
    wiek()

