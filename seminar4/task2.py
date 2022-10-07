# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число N: "))

list = []
i = 2
N = number

if number <= 0:
    print("Введите число больше нуля!")
else:
    while number != 1:
        if number % i == 0:
            list.append(i)
            number /= i
        else:
            i += 1
    print(f"Число {N}, разложенное на простые множетели = {list}")

# ещё
number = int(input("Введите число N: "))

list = []
i = 2

while number > 2:
    if number % 2 != 0:
        i += 1
    else:
        number //= i
        list.append(i)
print(list)