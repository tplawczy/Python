# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# def wykonaj():
# Use a breakpoint in the code line below to debug your sc
import array as arr
import copy
from typing import Optional, List


class Tablice():
    def __new__(self, pocz1):
        self.pocz1 = pocz1

        list = []
        list1 = [(self.pocz1)]
        list.append(list1)

        for i in range(1, self.pocz1 + 1):
            var = copy.deepcopy(list1)
            var.append(self.pocz1 + i)
            list1 = var
            list.append(var)

        return list

    def __init__(self, pocz):
        self.pocz =pocz
        Tablice(pocz)

def main():
    t = Tablice(3)
    # print(t[1])

    # print(t[2])
    for i in t:
        print(i)
        if len(i) >= 6:
            break

    t = Tablice(9)
    for i in t:
        print(i)
        if len(i) >= 7:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__'"":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
