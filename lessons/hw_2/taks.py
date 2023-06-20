# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число для перевода в шестнадцатеричное представление: '))

SYSTEM_16 = 16
digits = '0123456789abcdefg'

print(f'Проверка: {num} в шестнатиричной системе = {hex(num)}')

res = ''

while num > 0:
    i = num % SYSTEM_16
    res += digits[i]
    num //= SYSTEM_16
print(f'Результат перевода в шестнатиричную систему = {res[::-1]}')




# Напишите программу, кот. принимает две строки вида 'a/b' - дробь
# Программа должна возвращать сумму и произведение дробей.
# Для проверки используйте модуль fractions

import math

def sum_fractions(num_frac_1, num_frac_2):
    sum_frac = [int(num_frac_1[0]) * int(num_frac_2[1]) \
                + int(num_frac_2[0]) * int(num_frac_1[1]), \
                int(num_frac_1[1]) * int(num_frac_2[0])]
    nod = math.gcd(sum_frac[0], sum_frac[1])                        #Наименьший общий делитель
    sum_frac = [int(sum_frac[0] / nod), int(sum_frac[1] / nod)]
    print('Cумма дробей = ', sum_frac[0], '/', sum_frac[1])

def mult_fractions(num_frac_1, num_frac_2):                          # Умножение дробей и приведение к НОД
    mult_frac = [int(num_frac_1[0]) * int(num_frac_2[0]),
                 int(num_frac_1[1]) * int(num_frac_2[1])]
    nod = math.gcd(mult_frac[0], mult_frac[1])
    mult_frac = [int(mult_frac[0] / nod), int(mult_frac[1] / nod)]
    print('Произведение дробей = ', mult_frac[0], '/', mult_frac[1])

def Main():
    number_frac_1 = str(input('Введите первое число вида a/b - ')).split('/')
    number_frac_2 = str(input('Введите второе число вида a/b - ')).split('/')
    sum_fractions(number_frac_1, number_frac_2)
    mult_fractions(number_frac_1, number_frac_2)
# Main()

