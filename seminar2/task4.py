# Реализуйте алгоритм перемешивания списка.

import random

size = int(input("Введите размер списка: "))

list = []
for i in range(size):
    list.append(random.randint(-10, 10 + 1))
print("Изначальный список --> ", list)
random.shuffle(list)
print ("Перемешанный список --> ", list)


# 2 способ с ручным перемешиванием
size = int(input("Введите размер списка: "))

list = []
for i in range(size):
    list.append(random.randint(-10, 10 + 1))
print("Изначальный список --> ", list)

new_list = []
for  i in range(0, len(list)):
    j = random.randrange(0, len(list))
    new_list.append(list[j])
    list.remove(list[j])
print("Перемешанный список --> ", new_list)