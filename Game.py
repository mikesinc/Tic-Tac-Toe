import random

#clear screen between moves
def clear_screen():
    print('\n' * 100)

#construct board
def display_board(board):
    clear_screen()
    print(' '.rjust(50) + board[7] + ' | ' + board[8] + ' | ' + board[9] + '\n'
     + ' '.rjust(50) + '==+===+==' + '\n'
     + ' '.rjust(50) + board[4] + ' | ' + board[5] + ' | '+ board[6] + '\n' 
     + ' '.rjust(50) + '==+===+==' + '\n'
     + ' '.rjust(50) + board[1] + ' | ' + board[2] + ' | ' + board[3] + '\n\n')

#Assign Players
def player_input():
    player1 = ''
    while player1 != 'X' and player1 != 'x' and player1 != 'O' and player1 != 'o':
        player1 = input("Player 1, choose 'X' or 'O'").upper()
    if player1 == 'X' or player1 == 'x':
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
        print('Player 1, your first')
        return True
    else:
        print('Player 2, your first')
        return False

#check if space is available on board
def space_check(board, position):
    return board[position] == ' '

#check if board is full
def full_board_check(board):
    for space in board:
        if space == ' ':
            return False
    return True

#choose position
def player_choice(board, player):
    hasSpace = False
    validEntry = False
    while hasSpace == False:
        while validEntry == False:   
            try:
                choice = input(f'{player}, choose a square (use your numpad)')
                intchoice = int(choice)
                if intchoice in range(1,10):
                    break
            except:
                display_board(board)
                print('Choose a valid number from your numpad!')
        if space_check(board, intchoice):
            hasSpace = True
            return intchoice
        else:
            display_board(board)
            print('already filled! Pick another square.')

#play again?
def replay():
    again = ''
    while again != 'y' and again != 'Y' and again != 'n' and again != 'N':
        again = input('Do you wish to play again? (Y/N)').lower()
    if again == 'y':
        return True
    else:
        return False

clear_screen()
print('Welcome to Tic Tac Toe!')

while True: 
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    player1_marker, player2_marker = player_input()
    
    #First Turn by Player 1 or 2
    if choose_first():
        #player 1 turn
        place_marker(board, player1_marker, player_choice(board, player1_marker))
        #player 2 turn
        place_marker(board, player2_marker, player_choice(board, player2_marker))
    else:
        #player 2 turn
        place_marker(board, player2_marker, player_choice(board, player2_marker))

    #loop turns until winner is found.
    while True:
        #player 1 turn
        if full_board_check(board):
            print("It's a draw!")
            break
        place_marker(board, player1_marker, player_choice(board, player1_marker))
        if win_check(board, player1_marker):
            print(f"Player 1 ('{player1_marker}') wins!")
            break
        
        #player 2 turn
        if full_board_check(board):
            print("It's a draw!")
            break
        place_marker(board, player2_marker, player_choice(board, player2_marker))
        win_check(board, player2_marker)
        if win_check(board, player2_marker):
            print(f"Player 2 ('{player2_marker}') wins!")
            break

    if not replay():
        break