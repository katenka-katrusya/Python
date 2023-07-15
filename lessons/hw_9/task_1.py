# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

from cmath import sqrt
import json
import csv
import random
from typing import Callable


ROWS_MIN = 100
ROWS_MAX = 1000
NUM_MIN = -100
NUM_MAX = 100

def create_csv():
    with open('coeff.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in range(random.randint(ROWS_MIN, ROWS_MAX)):
            writer.writerow([random.randint(NUM_MIN, NUM_MAX), random.randint(NUM_MIN, NUM_MAX),
                             random.randint(NUM_MIN, NUM_MAX)])


def processing_csv(func: Callable):
    create_csv()

    def wrapper():
        with open('coeff.csv', 'r', encoding='UTF-8') as file:
            data = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for coefficient in data:
                if coefficient and coefficient[0] != 0:
                    func(*coefficient)
    return wrapper


def json_result(func: Callable):
    result = []

    def wrapper(*args):
        roots = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        result.append(solve_dict)
        with open("total.json", 'w', encoding='UTF-8') as file:
            json.dump(result, file, indent=2)
        return roots
    return wrapper


@processing_csv
@json_result
def find_roots(*args):
    a, b, c = args
    discr = b * b - 4 * a * c
    if discr > 0:
        x1 = (-b + sqrt(discr)) / (2 * a)
        x2 = (-b - sqrt(discr)) / (2 * a)
        return str(x1), str(x2)
    elif discr == 0:
        x = -b / (2 * a)
        return str(x)

if __name__ == '__main__':
    find_roots()