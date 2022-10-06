# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

import random

num = int(input("Введите размер списка: "))

randomList = []
unique = []

for i in range(num):
    randomList.append(random.randint(0, 9))
print(f"Изначальный список = {randomList}")

for el in randomList:
    count = 0
    for el2 in randomList:
        if el == el2:
            count += 1
    if count == 1:
        unique.append(el)
print(f"Уникальный список = {unique}")
