"""
Создайте программу для игры в ""Крестики-нолики"".
"""

print("Игра: Крестики-нолики ")

board = list(range(1, 10))


def draw_board(bord):  # рисует игровое поле
    print("-" * 13)
    for i in range(3):
        print("|", bord[0 + i * 3], "|", bord[1 + i * 3], "|", bord[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_token):  # принимает ввод пользователя. Проверяет корректность ввода
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(bord):  # проверяет, выиграл ли игрок
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if bord[each[0]] == bord[each[1]] == bord[each[2]]:
            return bord[each[0]]
    return False


def main(bord):  # Функция запускает и управляет игровым процессом
    counter = 0
    win = False
    while not win:
        draw_board(bord)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(bord)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(bord)


main(board)

input("Нажмите Enter для выхода!")
