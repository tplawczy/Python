# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

n=5

def program(n):
    print(triangle(n))

def triangle(n):
    if n == 0:
        return []

    elif n == 1:
        return [1]
    else:
        new_row = [1]
    last_row = triangle(n - 1)
    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])
    new_row += [1]
    return new_row


if __name__ == '__main__':
    program(n+1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
