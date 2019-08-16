import random

#clear screen between moves
def clear_screen():
    print('\n' * 100)

#construct board
clear_screen()
def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3] + '\n'
     + board[4] + '|' + board[5] + '|'+ board[6] + '\n' 
     + board[7] + '|' + board[8] + '|' + board[9])

#Assign Players
def player_input():
    player1 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = input("Player 1, choose 'X' or 'O'")
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

#Place marker
def place_marker(board, marker, position):
    board[position] = marker
    display_board(board)
    
#check winner
def win_check(board, mark):
    if (board[1] == board[2] == board[3] == mark
     or board[4] == board[5] == board[6] == mark
     or board[7] == board[8] == board[9] == mark
     or board[1] == board[4] == board[7] == mark
     or board[2] == board[5] == board[8] == mark
     or board[3] == board[6] == board[9] == mark
     or board[1] == board[5] == board[9] == mark
     or board[7] == board[5] == board[3] == mark):
        return True
    else:
        return False

#choose first player
def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1, your first'
    else:
        return 'Player 2, your first'

#check if space is available on board
def space_check(board, position):
    return board[position] == ''

#check if board is full
def full_board_check(board):
    for space in board:
        if space == '':
            return False
    return True

#choose position
def player_choice(board):
    validchoice = False
    while validchoice == False:
        choice = int(input('Choose a square (on your numpad)'))
        if space_check(board, choice):
            validchoice = True
            return choice

#play again?
def replay():
    again = ''
    while again != 'y' and again != 'n':
        again = input('Do you wish to play again? (y/n)').lower()
    if again == 'y':
        return True
    else:
        return False

print('Welcome to Tic Tac Toe!')

while True:
    player1_marker, player2_marker = player_input()
    choose_first()
    game_on = True
    board = ['#','','','','','','','','','']

    while game_on:
        #player 1 turn
        full_board_check(board)
        place_marker(board, player1_marker, player_choice(board))
        win_check(board, player1_marker)

        #player 2 turn
        full_board_check(board)
        place_marker(board, player2_marker, player_choice(board))
        win_check(board, player2_marker)

    if not replay():
        break