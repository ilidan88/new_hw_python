"""
Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
"""

x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

def quarter(x ,y):
    if (x > 0) and (y > 0):
        res = "Точка лежит в 1 четверти"
    elif (x < 0) and (y > 0):
        res = "Точка лежит в 2 четверти"
    elif (x < 0) and (y < 0):
        res = "Точка лежит в 3 четверти"
    elif (x > 0) and (y < 0):
        res = "Точка лежит в 4 четверти"
    elif (x or y) == 0:
        res = "значения не должны равнятся нулю"
    return print(res)


quarter(x, y)