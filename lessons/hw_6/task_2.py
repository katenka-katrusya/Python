# 2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

BOARD_SIZE = 8
list_one = []
list_two = []


def inp():
    for i in range(BOARD_SIZE):
        new_list_one, new_list_two = \
            [int(s) for s in input(f'введите {i + 1} координаты ферзей на доске 8×8, через пробел: ').split()]
        list_one.append(new_list_one)
        list_two.append(new_list_two)


def check(list_one1, list_two1):
    correct = True
    for i in range(BOARD_SIZE):
        for j in range(i + 1, BOARD_SIZE):
            if list_one1[i] == list_one1[j] or list_two1[i] == list_two1[j] \
                    or abs(list_one1[i] - list_one1[j]) == abs(list_two1[i] - list_two1[j]):
                correct = False

    if correct is True:
        return False
    else:
        return True

if __name__ == '__main__':
    inp()
    print(list_one)
    print(list_two)
    print(check(list_one, list_two))