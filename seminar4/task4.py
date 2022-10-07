# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

# import random

# pathWrite = r'PythonSeminars\seminar4\text.txt'

# k = int(input("Введите максимальную степень многочлена: "))

# line = []

# for i in range(k+1):
#     line.append(random.randint(0, 100))

# equation = ''

# for i in range(k+1):
#     if i == 0:
#         if line[i] > 0:
#             equation = equation + ' + ' + str(line[i]) + ' = 0'
#         else:
#             equation = equation + ' = 0'
#     elif i == 1:
#         if line[i] > 1:
#             equation = str(line[i]) + 'x' + equation
#         elif line[i] == 1:
#             equation = 'x' + equation
#     else:
#         if line[i] > 1:
#             equation = str(line[i]) + 'x^' + str(i) + ' + ' + equation
#         if line[i] == 1:
#             equation = 'x^' + str(i) + ' + ' + equation

# line.reverse()
# print(line)

# try:
#     with open(pathWrite, 'w') as data:
#         file = data.write(equation)
# except:
#     print("Ошибка работы с файлом")





# решение с семинара:

from random import randint as rI

def createEquation():
    degree = int(input("Введите максимальную степень многочлена: "))
    equation = ''

    for d in range(degree, -1, -1):
        coef = rI(-20, 20)
        if d == degree:
            if coef > 0:
                equation += str(coef) + 'x^' + str(d)
            if coef < 0:
                equation += '-' + str(abs(coef)) + 'x^' + str(d)
        else:
            if coef > 0:
                equation += ' + ' + str(coef) + 'x^' + str(d)
            if coef < 0:
                equation += ' - ' + str(abs(coef)) + 'x^' + str(d)

    return equation + " = 0"

# Для следующей задачи нам нужны степени 1 и 0, поэтому закомментим всё после функции

# Заменяем неугодные моменты .replace('1' - что меняем, '2' - на что меняем)

# eq1 = createEquation()
# print((eq1.replace('x^1', 'x').replace('x^0', '')).replace('1x^', 'x^')) 
# eq2 = createEquation()
# print((eq2.replace('x^1', 'x').replace('x^0', '')).replace('1x^', 'x^'))

