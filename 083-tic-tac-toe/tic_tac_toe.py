from random import randrange

computer_symbol = "X"
user_symbol = "O"
board = []
game_end = False

def display_board(board):
    """
    The function accepts one parameter containing the board's current status
    and prints it out to the console.
    """    
    for r in range(3):
        print(board[r])
    #make_list_of_free_fields(board)
    print('\n')

def user_move(board):
    """
    The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision.
    """
    my_move = int(input("Choose your cell, from 1 to 9..."))
    if my_move < 0 or my_move not in range(1,10):
        print("Invalid cell. Must be between 1 and 9!")
        user_move(board)
        
    row = (my_move-1) // 3
    col = (my_move-1) - (3*row)
    #print(my_move, ': ', row,', ', col)
    if (row,col) not in make_list_of_free_fields(board):
        print("Cell already used!")
        user_move(board)

    board[row][col] = user_symbol

def make_list_of_free_fields(board):
    """
    The function browses the board and builds a list of all the free squares; 
    the list consists of tuples, while each tuple is a pair of row and column numbers.
    """
    free_fields = []
    for r in range(3):    
        for c in range(3):            
            if board[r][c] not in ( computer_symbol , user_symbol):                
                free_fields.append((r,c))

    print('Free (', len(free_fields), '): ' ,  free_fields)
    return free_fields

def victory_for(board, sign):
    """
    The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game
    """
    global game_end
    
    for r in range(3):    
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            print('Victory for symbol ' , sign, ' in row ', r)
            game_end = True
            return

    for c in range(3):    
        if board[0][c]==sign and board[1][c]==sign and board[2][c] ==sign:
            print('Victory for symbol ' , sign, ' in column ', c)
            game_end = True
            return

    if board[0][0]==sign and board[1][1]==sign and board[2][2] ==sign:
            print('Victory for symbol ' , sign, ' in diagonal')
            game_end = True
            return

    if board[0][2]==sign and board[1][1]==sign and board[2][0] ==sign:
            print('Victory for symbol ' , sign, ' in diagonal')
            game_end = True
            return

    
    availables = 0
    for r in range(3):    
            for c in range(3):            
                if board[r][c] not in ( computer_symbol , user_symbol):   
                    availables += 1

    if availables == 0:
        print('Tie (no available squares')
        game_end = True
        return

    print('Available squares: ',availables)

def computer_move(board):
    """
    Draws the computer's move and updates the board.
    """
    _move = randrange(1,10)
    row = (_move-1) // 3
    col = (_move-1) - (3*row)
    print('Computer move:', '(', row,', ', col, ')')   

    if (row,col) not in make_list_of_free_fields(board):   
        print('Computer move not available. Retrying...')     
        computer_move(board)
    else:         
        board[row][col] = computer_symbol
    return 


print('Begin..')
# initial board
for i in range(3):    
    row = [(3*i)+j+1 for j in range(3)]
    board.append(row)    

display_board(board)
print('Computer first move..')
board[1][1] = computer_symbol 
display_board(board)

while not game_end:
    user_move(board)
    victory_for(board, user_symbol)    
    display_board(board)
    
    if game_end == False:
        computer_move(board)
        victory_for(board, computer_symbol)
        display_board(board)
else:
  print("Exited game")