while True:
    print('Welcome to this game of Xs and Os')

    def startGame():
        start = 'Wrong'
        while start not in ['Y', 'N']:
            start = input("Would you like to start (Y or N)?: ")

            if start not in ['Y', 'N']:
                print('That is not a valid character :(')
        return start

    board =[' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' '] 

    def display_board(board):
        print(' {} | {} |  {} '. format(board[0],board[1],board[2]))
        print('-----------')
        print(' {} | {} |  {} '.format(board[3],board[4],board[5]))
        print('-----------')  
        print(' {} | {} |  {} '.format(board[6],board[7],board[8]))

    def player_input():
        player1 = 'wrong'
        while player1 not in range(0,9):

            player1 = int(input("Please pick a number from 0 to 8:  ")) 

            if player1 not in range(0,9):
                print("Select a valid numebr within the range")

        if player1 in range(0,9):
            return int(player1)

    def check_win(board, mark):
        if(board[0]== mark and board[1] == mark and board[2] == mark):
            return True
        elif(board[3]== mark and board[4] == mark and board[5] == mark):
            return True
        elif(board[6]== mark and board[7] == mark and board[8] == mark):
            return True
        elif(board[0]== mark and board[3] == mark and board[6] == mark):
            return True
        elif(board[1]== mark and board[4] == mark and board[7] == mark):
            return True
        elif(board[2]== mark and board[5] == mark and board[8] == mark):
            return True
        elif(board[0]== mark and board[4] == mark and board[8] == mark):
            return True
        elif(board[2]== mark and board[4] == mark and board[6] == mark):
            return True
        else:
            return False

    start = startGame()
    X_move = True
    

    while start == 'Y':

        while X_move:
            display_board(board)
            player_move = player_input()
            
            if board[player_move] == ' ':
                board[player_move] = 'X'    
                if check_win(board, 'X'):
                    print('X wins!')
                    start = 'N'
                X_move = False
            else:
                print("That move is not allowed")

        while X_move == False and start == 'Y':
            display_board(board)
            player_move = player_input()
            
            if board[player_move] == ' ':
                board[player_move] = 'O'    
                if check_win(board, 'O'):
                    print('O wins!')
                    start = 'N'
                X_move = True
            else:
                print("That move is not allowed")


    

 


        



