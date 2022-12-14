"""
Пройтись по своим предыдущим ДЗ и где возможно использовать ускореную обработку данных
"""

#  Пример 1:
import random

original_list = [1, 2, 3, 4, 5, 6]
print(original_list)
random.shuffle(original_list)
print(original_list)


#  Пример 2:

lst = [2, 3, 5, 9, 3]
sum = 0
for i, a in enumerate(lst):
    if i % 2 != 0:
        sum += int(a)
print(sum)


# Пример 3
lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
print(max(new_lst) - min(new_lst))