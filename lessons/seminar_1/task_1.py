# Пользователь вводит число от 1 до 999. Сообщите, что введено: цифра, двузначное число или трёхзначное.
# Для цифры верните её квадрат (5 - 25)
# Для двузн. числа произведение цифр (30 - 0)
# Для трёхзн. числа его зеркальное отображение (520 - 25)
# Если число не из диапазона, запросите новое число

MIN_LIMIT = 1
MAX_LIMIT = 999

LEN_1 = 1
LEN_2 = 10
LEN_3 = 100

while True:
    print('Введите целое число от', MIN_LIMIT, 'до', MAX_LIMIT, ': ')
    num = int(input())
    if num < MIN_LIMIT or num > MAX_LIMIT:
        print('Введите число из диапазона')
    else:
        break

if len(str(num)) == len(str(LEN_1)):
    print('Возводим в квадрат: ', num ** 2)
elif len(str(num)) == len(str(LEN_2)):
    mult = 1
    while (num != 0):
        mult *= (num % 10)
        num //= 10
    print("Произведение цифр равно: ", mult)
elif len(str(num)) == len(str(LEN_3)):
    revert = str(num)[::-1]
    print('Зеркальное отображение числа: ', revert)