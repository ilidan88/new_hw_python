"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
Пример:
45 -> 101101
3 -> 11
2 -> 10
"""

binary = ""
user_input = 45 #int(input("Введите число для преобразовывания:\n"))
while user_input != 0:
    binary = str(user_input % 2) + binary
    user_input //= 2
print(binary)