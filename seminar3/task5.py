# Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

size = int(input("Введите размер списка: "))

# Первая фунция с положительными индексами
def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

list = []

# Складываем в первый список
for el in range(1, size+1):
    list.append(fibonacci(el))

# Вторая фунция с отрицательными индексами
def negafibonacci(n):
    if n in [-1]:
        return 1
    if n in [-2]:
        return -1
    else:
        return negafibonacci(n+2) - negafibonacci(n+1)
        
list2 = []

# Складываем во второй список. Начинаем с -size, список сразу переворачивается, не надо делать reverse. 
# Добавляем в конец списка - ноль.
for el in range(-size, 0):
    list2.append(negafibonacci(el))
list2.append(0)

# Добавляем во второй список - первый, чтобы получить один большой с отрицательными индексами и положительными
for i in range (1, size+1):
    list2.append(fibonacci(i))
print(list2)

