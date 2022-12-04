"""
Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

lst = [2, 3, 5, 9, 3]


def odd(list_of_elements):
    res = 0
    for i in range(len(list_of_elements)):
        if i % 2 != 0:
            res += list_of_elements[i]
    return res

print(odd(lst))

