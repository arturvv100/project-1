from IPython.display import clear_output
import random

test_table = ['#','X','O','X','O','X','O','X','O']

#------------------------------------------------------------

def display_game(table):
    print(f' {table[0]} | {table[1]} | {table[2]} ')
    print('-----------') 
    print(f' {table[3]} | {table[4]} | {table[5]} ')
    print('-----------') 
    print(f' {table[6]} | {table[7]} | {table[8]} ')

#------------------------------------------------------------

def user_choice():
    within_range = False
    choice = 'Wrong'
    acceptable_range = range(1,10)
    while choice.isdigit() == False or within_range == False:
        choice = input('Podaj wartość (1-9): ')
        if choice.isdigit() == False:
            print('Podana wartość nie jest cyfrą')
        else:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print('Podana wybór jest poza zakresem 0-9')
    return int(choice)

#------------------------------------------------------------

def space_check(table, position):
    return table[int(position)-1] == ' '

#------------------------------------------------------------

def full_board_check(table):
    full = True
    for i in table:
        if i == ' ':
            full = False
    return full

#------------------------------------------------------------

def replay():
    choice = 'Wrong'
    while choice not in ['Y','N']:
        choice = input('Czy chcesz zagrać jeszcze raz? (Y lub N)')
        if choice not in ['Y','N']:
            print('Niepoprawna odpowiedź, wybierz Y lub N ')
    if choice == 'Y':
        return True
    else:
        return False

#------------------------------------------------------------

def player_input():
    choice = 'Wrong'
    while choice not in ['X','O']:
        choice = input('Gracz 1: wybierz X lub O ')
        if choice not in ['X','O']:
            print('Niepoprawna odpowiedź, wybierz X lub O ')
    if choice == 'X':
        return 'X'
    else:
        return 'O'

#------------------------------------------------------------

def replace_position(position,mark):
    global table
    if table[position-1] == ' ':    
        if mark == 'X':
            table[position-1] = 'X'
        else:
            table[position-1] = 'O'

#------------------------------------------------------------

def check(table,mark):
    checklist = [[0,1,2],[3,4,5],[6,7,8],
                 [0,3,6],[1,4,7],[2,5,8],
                 [0,4,8],[2,4,6]
                ]
    win = False
    for i in checklist:
        k = ['','','']
        for j in range (0,3):
            if table[i[j]] == mark:
                k[j] = mark
        if k[0] == mark and k[1] == mark and k[2] == mark:
            win = True
    return win

#------------------------------------------------------------

def choose_first():
    x = random.randint(0,1)
    if x == 0:
        return 'X'
    else:
        return 'O'

#Game starts here--------------------------------------------

game_on = True
player = ['','']
print('Witaj w grze kółko i krzyżyk')

while True:
    gracz = player_input()
    gracz1 = choose_first()
    if gracz1 == 'X':
        player[0] = 'X'
        player[1] = 'O'
    else:
        player[0] = 'O'
        player[1] = 'X'
    clear_output()
    print(f"Zaczyna {gracz1}")
    table = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_game(table)
    
    while game_on:
        position = int(user_choice())
        while space_check(table, position) == False:
            print('Podana pozycja jest zajęta')
            position = int(user_choice())
        replace_position(position,player[0])
        clear_output()
        display_game(table)
        if check(table,player[0]):
            print(f'Gracz {player[0]} wygrywa !')
            break
        if full_board_check(table):
            print('Remis !')
            break
        position = int(user_choice())
        while space_check(table, position) == False:
            print('Podana pozycja jest zajęta')
            position = int(user_choice())
        replace_position(position,player[1])
        clear_output()
        display_game(table)
        if check(table,player[1]):
            print(f'Gracz {player[0]} wygrywa !')
            break        
    if not replay():
        break
    else:
        clear_output()