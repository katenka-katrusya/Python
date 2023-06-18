# year = int(input('Введите год в формате уууу: '))
# if year % 4 != 0:
#     print('Обычный год')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('Високосный')
#     else:
#         print('Обычный')
# else:
#     print('Високосный')


# Код короче:
year = int(input('Введите год в формате уууу: '))
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print('Обычный год')
else:
    print('Високосный')
