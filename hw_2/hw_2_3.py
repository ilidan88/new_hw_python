"""
Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
"""
import random

original_list = [1, 2, 3, 4, 5, 6]


def randomizer (list_original):
    new_list = list_original
    list_len = len(new_list)
    for i in range(list_len):
        index_list = random.randint(0, list_len - 1)
        new_index = new_list[i]
        new_list[i] = new_list[index_list]
        new_list[index_list] = new_index
    return new_list

print(randomizer(original_list))

