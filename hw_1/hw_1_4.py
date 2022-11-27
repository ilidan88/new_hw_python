
"""
Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y)
"""

import random

x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))


def quarter(x, y):
    if (x > 0) and (y > 0):
        res = 1
    elif (x < 0) and (y > 0):
        res = 2
    elif (x < 0) and (y < 0):
        res = 3
    elif (x > 0) and (y < 0):
        res = 4
    elif (x or y) == 0:
        res = "значения не должны равнятся нулю"
    return res


if quarter(x, y) == 1:
    for i in range(0, 10):
        print(i)
elif quarter(x, y) == 2:
    for i in range(-5, 5):
        print(i)
elif quarter(x, y) == 3:
    for i in range(-10, 0):
        print(i)
elif quarter(x, y) == 4:
    for i in reversed(range(-5, 5)):
        print(i)
else:
    print("значения не должны равнятся нулю")



