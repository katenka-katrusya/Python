# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30

# 1 способ, нормальный:
num = int(input("Введите число: "))
if num % 30 == 0:
    print("Число кратно 30, введите другое число")
elif (num % 5 == 0) and (num % 10 == 0): 
    print("Число кратно одновременно и 5 и 10")
elif num % 15 == 0:
    print("Число кратно 15")
else:
    print("Число не кратно 5 и 10 или 15")


# 2 способ, отвечающий ТЗ, не очень нормальный:

num = int(input("Введите число: "))
if ((num % 5 == 0) and (num % 10 == 0) or (num % 15 == 0)) and (num % 30 != 0):
    print("Кратно")
else:
    print ("Не кратно")