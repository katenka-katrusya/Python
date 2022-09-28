# Реализуйте алгоритм перемешивания списка.

import random

size = int(input("Введите размер списка: "))

list = []
for i in range(size):
    list.append(random.randint(-10, 10 + 1))
print("Изначальный список --> ", list)
random.shuffle(list)
print ("Перемешанный список --> ", list)

