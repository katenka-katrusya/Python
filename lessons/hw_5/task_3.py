# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

num = int(input('Введите число: '))
first_num = 0

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

print(first_num, *fibonacci(num))
