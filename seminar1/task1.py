# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры: - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

num = int(input("Введите положительное число: "))
if num < 0:
    print("Введите положительное число!")
else:
    for i in range(-num, num + 1):
        print(i, end = " ") 


# 2 способ:

N = int(input("Введите число N: "))

listInt = []
i = -N
while i <= N:
    listInt.append(i)
    i += 1

print(listInt)
