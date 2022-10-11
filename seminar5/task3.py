# Создайте программу для игры в "Крестики-нолики"

board = list(range(1,10))

def draw_board(board):                 # Чертим поле
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_sign):          # Ввод данных в игру. Функция изменяет имеющийся список board
    valid = False
    while not valid:
        player_answer = input(f"В какую ячейку поместим {player_sign}? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод, введите число: ")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_sign
                valid = True
            else:
                print ("Место занято")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):           # Проверка игрового поля
    win_line = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))  
    for element in win_line:     
        if board[element[0]] == board[element[1]] == board[element[2]]:   # Если символы во всех трех заданных клетках равны, то выигрыш
            return board[element[0]]
    return False

def main(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        count += 1
        if count > 4:
            mark = check_win(board)
            if mark:
                print (f"\n{mark}выиграл!")
                win = True
                break
        if count == 9:
            print ("\nНичья!")
            break
    draw_board(board)

main(board)