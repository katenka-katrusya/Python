pwd = 'text'
res = input('Введите пароль: ')
if res == pwd:
    print('Доступ разрешён')
    my_match = int(input('2 + 2 = '))
    if 2 + 2 == my_match:
        print('Ура! Правильно')
    else:
        print('Очень жаль, но не так')
else:
    print('Error')


