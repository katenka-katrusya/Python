# Создайте программу для игры с конфетами человек против человека. У меня без бота, я запуталась, сложнааа.

from random import choice, randint

welcome_text = ('\nДобро пожаловать в игру! Запаситесь конфетами и чаем, вжух!\n'
                'Правила таковы: на столе лежат 150 конфет, вы берёте их поочереди.\n'
                'За один раз можно взять максимум 28 конфет.\n'
                'Выигрывает тот, кто последний заберёт все конфеты.\n'
                'Да начнутся игры!')
print(welcome_text)

messages = ['Твой ход брать конфеты,', 'Сколько желаете конфет?',
            'Сколько конфет берем?', 'Возьми конфетку,', 'Твой ход,']

def player_vs_player():
    max_candies = 150
    max_take = 28
    count = 0
    player_1 = input('\nИмя первого игрока: ')
    player_2 = input('\nИмя второго игрока: ')

    print('\nДля начала опеределим кто первый начнет игру с помощью жеребьёвки:\n')

    lot = randint(1, 2)
    if lot == 1:
        first = player_1
        second = player_2
    else:
        first = player_2
        second = player_1

    print(f'Мои поздравления {first}, ты ходишь первым!')

    while max_candies > 0:

        if count == 0:
            move = int(input(f'\nУ нас {max_candies} конфет на столе. {choice(messages)} {first}: '))       
            
            if move > max_candies or move > max_take or move < 1:
                move = int(input(f'\nМожно взять от 1 до {max_take} конфет, {first}, попробуй еще раз: '))
        
            max_candies = max_candies - move

        if max_candies > 0:
            count = 1
        else:
            print('GAME OVER')

        if count == 1:
            move = int(input(f'\nОсталось {max_candies} вкусняшек. {choice(messages)} {second}: '))   
            
            if move > max_candies or move > max_take or move < 1:
                move = int(input(f'\nМожно взять от 1 до {max_take} конфет, попробуй еще раз: '))

            max_candies = max_candies - move

        if max_candies > 0:
            count = 0
        else:
            print('Конфеток больше нет!')

    if count == 0:
        print(f'Наш победитель - {first}')
    if count == 1:
        print(f'Наш победитель - {second}')

player_vs_player()