# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# num = int(input("Введите число: "))

# result = {}
# for n in range(1, num + 1):
#     result[n] = round((1 + 1/n)**n, 2)
# print("Список:", result)
# print(f"Сумма чисел = {sum(result)}")

# переделала на равильный вариант
number = int(input("Введите число: "))
list = []
for n in range(1, number + 1):
    result = round((1 + (1 / n)) ** n, 2)
    list.append(result)
print(f"Cписок чисел: {list}")
print(f"Сумма чисел = {sum(list)}")