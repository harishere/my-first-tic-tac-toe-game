'''
Milestone Project-1: Tic Tac Toe

'''

#Importing clear_output function to clearn screen
#from IPython.display import clear_output

#importing random for first player turn
import random

#Configuring the board
board = [' '] * 9

def display_board(board):
    #Game board screen using indexing method
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[0] + '|' + board[1] + '|' + board[2])

def player_input():
    #selecting the market i.e. X or O by Player-1 or Player-2

    global player1
    global player2

    player1 = input('Player-1: Please choose your marker: "X" or "O" = ').upper()

    if player1 == 'X' or player1 == 'O':
        pass

    else:
           
        while player1 != 'X' or player1 != "O":
            player1 = input('Player-1: Please choose from: "X" or "O" = ').upper()
            if player1 == "X" or player1 == "O":
                break

    if player1 == "X":
        player2="O"
    else:
        player2 = "X"
    

    print('Player-1: ', player1)
    print('Player-2: ', player2)

def win_check(board, mark):
    #checking if any player has won

    if mark == board[0] and mark == board[1] and mark == board[2]:
        return True
    
    elif mark == board[0] and mark == board[3] and mark == board[6]:
        return True
    
    elif mark == board[0] and mark == board[4] and mark == board[8]:
        return True
    
    elif mark == board[1] and mark == board[4] and mark == board[7]:
        return True
    
    elif mark == board[2] and mark == board[4] and mark == board[6]:
        return True
    
    elif mark == board[2] and mark == board[5] and mark == board[8]:
        return True
    
    elif mark == board[3] and mark == board[4] and mark == board[5]:
        return True
    
    elif mark == board[3] and mark == board[4] and mark == board[5]:
        return True
    
    else:
        return False

def choose_first():
    #random selection of a player:

    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def place_marker(board, marker, position):
    
    board[position] = marker
    return

def space_check(board, position):
    #chcking is a marker is placed or the location is empty
    return board[position] == ' '

def full_board_check(board):
    #checking if the board is full
    for i in range(1,10):
         if space_check(board, i):
            return True
    return False
    

def player_choice(board,n):
    player_position = 0

    player_position = int(input(f"Player-{n}: Enter your position (position: 1-9): "))
    
    if space_check(board, player_position-1) is True: #Means spare
        return player_position-1


print('Welcome to Tic Tac Toe!\n')

player_input()
display_board(board)

if full_board_check(board) is True:


    while full_board_check(board) is True:

        #player-1
        place_marker(board, player1, player_choice(board,1))
        display_board(board)

        if win_check(board, player1) is True:
            print(f'Player-1 Won!!!')
            break

        #player-2
        place_marker(board, player2, player_choice(board,2))
        display_board(board)
        
        if win_check(board, player2) is True:
            print(f'Player-2 Won!!!')
            break











