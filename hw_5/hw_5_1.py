"""
Создайте программу для игры с конфетами человек против компьютера.
Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Подумайте как наделить бота ""интеллектом""
"""
from random import randint

All_candies = 150
take_candies = 0
player_candies = 0
bot_candies = 0


def who_goes_first():
    random_number = randint(1, 2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()


def player_turn():
    global All_candies
    global take_candies
    global player_candies
    print(f"Ваш ход, на столе {All_candies} концет")
    take_candies = int(input("Сколько хотите взять ?:  "))
    while take_candies > 28 or take_candies < 0 or take_candies > All_candies:
        take_candies = int(input("За раз можно взять не более 28 конфет: "))
    All_candies -= take_candies
    player_candies += take_candies
    if All_candies > 0:
        bot_turn()
    else:
        print("Вы победили")


def bot_turn():
    global All_candies
    global take_candies
    global bot_candies
    take_candies = All_candies % 29 if All_candies % 29 != 0 else randint(1, 28)
    All_candies -= take_candies
    bot_candies += take_candies
    print(f"Бот взял {take_candies} конфет")
    if All_candies > 0:
        player_turn()
    else:
        print("Вы проиграли")


who_goes_first()