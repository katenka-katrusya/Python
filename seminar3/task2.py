# Напишите программу, которая найдёт произведение пар чисел списка (Список создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

size = int(input("Введите размер списка: "))
list = []
new_list = []

for i in range(size):
    list.append(random.randint(0, 10))
print(f"Список = {list}")

for i in range(len(list) // 2):
    while len(list) > 1:
        new_list.append(list[0] * list[-1])
        list.pop(0)
        list.pop(-1)
        if len(list) == 1: 
            new_list.append(list[0] ** 2)
print(f"Произведение пар чисел = {new_list}")