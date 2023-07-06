# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import task_2 as task
import random


BOARD_SIZE = 8
OPTIONS = 4


def rand(size):
    res = []
    i = 0
    while i < size:
        gen = [random.randint(0, size), random.randint(0, size)]
        i += 1
        if gen in res:
            i -= 1
        else:
            res.append(gen)
    return res

def my_func():
    count = 0
    count_attempt = 0
    while count < OPTIONS:
        count_attempt += 1
        win_list = rand(BOARD_SIZE)
        win = list(win_list)
        new_x, new_y = map(list, zip(*win_list))
        if task.check(new_x, new_y):
            print(f'{count_attempt}. {win}')
            count += 1


if __name__ == '__main__':
    print('Успешные расстановки: ')
    my_func()