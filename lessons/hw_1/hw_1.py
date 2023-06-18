# def Main():
#     print('Введите стороны треугольника a, b, c:')
#     a = float(input('a = '))
#     b = float(input('b = '))
#     c = float(input('c = '))
#     print(triangle(a, b, c))
#
# def triangle(a, b, c):
#     if (a == b) and (b == c):
#         return 'Треугольник равносторонний'
#     elif ((a == b) or (a == c) or (b == c)) and (a + b > c) and (a + c > b) and (b + c > a):
#         return 'Треугольник равнобедренный'
#     elif (a + b > c) and (a + c > b) and (b + c > a):
#         return 'Треугольник существует'
#     else:
#         return 'Треугольника не существует'
#
# Main()


flag = True
MAX_NUM = 100000

while True:
    print('Введите число от 1 до', MAX_NUM, '= ', end='')
    num = int(input())
    if (num > 0) and (num < MAX_NUM):
        break
for i in range(2, num // 2):
    if num % i == 0:
        flag = False
        break
if flag: print('Число', num, 'простое')
else: print('Число', num, 'составное')
