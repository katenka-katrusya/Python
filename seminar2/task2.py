# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


N = int(input("Введите число: "))

result = []
count = 1
if N == 0 or N == 1:
    print(f"Факториал числа {N} = 1")
else:
    for i in range(N):  
        count *= i + 1  
        result.append(count)    
print(f"Факториал числа {N} = {count}. Набор произведений числа {N} = {result}")