"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
6782 -> 23
0,56 -> 11
"""

a = input("Введите число: ")


def num_sum(num):
    b = 0
    for i in num:
        if i.isdigit():
            b += int(i)
        else:
            continue
    return print(b)


num_sum(a)
