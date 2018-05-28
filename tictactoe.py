#from IPython.display import clear_output

def display_board(board):
    
    print('  {} | {} | {}'.format(board[7], board[8], board[9]))
    print('---------------')
    print('  {} | {} | {}'.format(board[4], board[5], board[6]))
    print('---------------')
    print('  {} | {} | {}'.format(board[1], board[2], board[3]))

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = raw_input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    
    if board[1] == mark and board[2] == mark and board[3] == mark: #horizontal
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark: #horizontal
        return True
    elif  board[7] == mark and board[8] == mark and board[9] == mark: #horizontal
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark: #vertical
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark: #vertical
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark: #vertical
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark: #diagonal
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark: #diagonal
        return True
    else:
        return False

import random

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    #print(board[position] == ' ')
    #print(position)
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(raw_input('Choose your next position: (1-9) ')) 
       # print(full_board_check(board))
        if full_board_check(board):
            print("It's a tie!")
            position = 500
            break
    return position

def replay():
    response = raw_input("Do you want to play again? Enter y or n: ")
    if response == 'y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    #Set up board and have player pick their marker
    board = [' ']* 10
    player1, player2 = player_input()
    
    #Choose who will go first
    turn = choose_first()
    print( turn + ' will go first.')
    
    ready = raw_input('Are you ready ' + turn + '? Enter y or n: ')
    if ready == 'y':
        game_on = True
    else:
        game_on = False
    
    
    while game_on:
        # Player 1's Turn
        if 'Player 1' == turn:
            
            display_board(board)
            #Pick position
            position = player_choice(board)
            if position == 500:
                break
            #Check if position is available
            result = space_check(board, position)
            #If it is available, mark the position
            if result:
                place_marker(board, player1, position)
                #Check if player 1 has won
                didyouwin = win_check(board, player1)
                if didyouwin:
                    display_board(board)
                    print("Congrats Player 1, you won!")
                    break
            
                #if no tie, player 2's turn
                print("Now it's Player 2's turn!")
                turn = 'Player 2 '

                
        else:
            display_board(board)
            #Pick position
            position = player_choice(board)
            if position == 500:
                break
            #Check if position is available
            result = space_check(board, position)
            #If it is available, mark the position
            if result:
                place_marker(board, player2, position)
                #Check if player 1 has won
                didyouwin = win_check(board, player2)
                if didyouwin:
                    display_board(board)
                    print("Congrats Player 2, you won!")
                    break

                #if no tie, player 2's turn
                print("Now it's Player 1's turn!")
                turn = 'Player 1'

            
        

    if not replay():
        break