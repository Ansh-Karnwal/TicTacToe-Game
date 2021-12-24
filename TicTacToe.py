class TicTacToe:
    #board creation
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def __init__(self):
      #initalizing board
      self.get_board()
      self.player_validation()
      
    def isPlaceValid(self, num):
        #checks if numbers between or are 1 and 9 and returns true if thats the case otherwise returns false
        if num >= 1 and num <= 9:
            return True
        return False

    def player_validation(self):
        #runs validator 9 times
        for i in range(9):
            #infinite loop to force valid input 
            while True:
                try:
                    self.player_1 = int(input('Where does Player 1 move: '))
                    #validates input
                    while not self.isPlaceValid(self.player_1): 
                        print('Sorry, illegal input! Please input again.')
                        self.player_1 = int(input('Where does Player 1 move: '))
                    #calls isSpotChosen function to validate input  
                    while self.isSpotChosen(self.player_1):
                        print('Sorry, spot has been chosen please chose another')
                        self.player_1 = int(input('Where does Player 1 move: '))
                    #calls isPlaceValid function to validate input
                        while not self.isPlaceValid(self.player_1):
                            print('Sorry, illegal input! Please input again.')
                            self.player_1 = int(input('Where does Player 1 move: '))
                    #puts X or O on the board
                    self.board_player_1_place()
                    #calls the board to put onto screen
                    self.get_board()
                    #checks if player has won
                    self.win_validation()
                    break 
                except ValueError:
                    print('Sorry, illegal input! Please input again.')
            #checks if board is full if it is quits the program        
            if self.isBoardFull():
                print('Its a tie!')
                quit()
            #same thing as above
            while True:
                try:
                    self.player_2 = int(input('Where does Player 2 move: '))

                    while self.player_2 < 1 or self.player_2 > 9: 
                        print('Sorry, illegal input! Please input again.')
                        self.player_2 = int(input('Where does Player 2 move: '))
                        
                    while self.isSpotChosen(self.player_2):
                        print('Sorry, spot has been chosen please chose another')
                        self.player_2 = int(input('Where does Player 2 move: '))

                        while not self.isPlaceValid(self.player_2):
                            print('Sorry, illegal input! Please input again.')
                            self.player_2 = int(input('Where does Player 2 move: '))

                    self.board_player_2_place()
                    self.get_board()
                    self.win_validation()
                    break 
                except ValueError:
                    print('Sorry, illegal input! Please input again.')
            
    #replaces number values on board with X 
    def board_player_1_place(self):
        if self.player_1 == 1: TicTacToe.board.pop(0), TicTacToe.board.insert(0, 'X')
        if self.player_1 == 2: TicTacToe.board.pop(1), TicTacToe.board.insert(1, 'X')
        if self.player_1 == 3: TicTacToe.board.pop(2), TicTacToe.board.insert(2, 'X')
        if self.player_1 == 4: TicTacToe.board.pop(3), TicTacToe.board.insert(3, 'X')
        if self.player_1 == 5: TicTacToe.board.pop(4), TicTacToe.board.insert(4, 'X')
        if self.player_1 == 6: TicTacToe.board.pop(5), TicTacToe.board.insert(5, 'X')
        if self.player_1 == 7: TicTacToe.board.pop(6), TicTacToe.board.insert(6, 'X')
        if self.player_1 == 8: TicTacToe.board.pop(7), TicTacToe.board.insert(7, 'X')
        if self.player_1 == 9: TicTacToe.board.pop(8), TicTacToe.board.insert(8, 'X')

    #replaces number values on board with O 
    def board_player_2_place(self):
        if self.player_2 == 1: TicTacToe.board.pop(0), TicTacToe.board.insert(0, 'O')
        if self.player_2 == 2: TicTacToe.board.pop(1), TicTacToe.board.insert(1, 'O')
        if self.player_2 == 3: TicTacToe.board.pop(2), TicTacToe.board.insert(2, 'O')
        if self.player_2 == 4: TicTacToe.board.pop(3), TicTacToe.board.insert(3, 'O')
        if self.player_2 == 5: TicTacToe.board.pop(4), TicTacToe.board.insert(4, 'O')
        if self.player_2 == 6: TicTacToe.board.pop(5), TicTacToe.board.insert(5, 'O')
        if self.player_2 == 7: TicTacToe.board.pop(6), TicTacToe.board.insert(6, 'O')
        if self.player_2 == 8: TicTacToe.board.pop(7), TicTacToe.board.insert(7, 'O')
        if self.player_2 == 9: TicTacToe.board.pop(8), TicTacToe.board.insert(8, 'O')

    #checks if any player has won 8 patterns of winning total
    def win_validation(self):
        #horizontal wins
        if TicTacToe.board[0] == 'X' and TicTacToe.board[1] == 'X' and TicTacToe.board[2] == 'X': print('Player 1 Won!'), quit()
        if TicTacToe.board[3] == 'X' and TicTacToe.board[4] == 'X' and TicTacToe.board[5] == 'X': print('Player 1 Won!'), quit()
        if TicTacToe.board[6] == 'X' and TicTacToe.board[7] == 'X' and TicTacToe.board[8] == 'X': print('Player 1 Won!'), quit()
        if TicTacToe.board[0] == 'O' and TicTacToe.board[1] == 'O' and TicTacToe.board[2] == 'O': print('Player 2 Won!'), quit()
        if TicTacToe.board[3] == 'O' and TicTacToe.board[4] == 'O' and TicTacToe.board[5] == 'O': print('Player 2 Won!'), quit()
        if TicTacToe.board[6] == 'O' and TicTacToe.board[7] == 'O' and TicTacToe.board[8] == 'O': print('Player 2 Won!'), quit()
        
        #vertical wins
        if TicTacToe.board[0] == 'X' and TicTacToe.board[3] == 'X' and TicTacToe.board[6] == 'X': print('Player 1 Won!'), quit()
        if TicTacToe.board[1] == 'X' and TicTacToe.board[4] == 'X' and TicTacToe.board[7] == 'X': print('Player 1 Won!'), quit()
        if TicTacToe.board[2] == 'X' and TicTacToe.board[5] == 'X' and TicTacToe.board[8] == 'X': print('Player 1 Won!'), quit()
        if TicTacToe.board[0] == 'O' and TicTacToe.board[3] == 'O' and TicTacToe.board[6] == 'O': print('Player 2 Won!'), quit()
        if TicTacToe.board[1] == 'O' and TicTacToe.board[4] == 'O' and TicTacToe.board[7] == 'O': print('Player 2 Won!'), quit()
        if TicTacToe.board[2] == 'O' and TicTacToe.board[5] == 'O' and TicTacToe.board[8] == 'O': print('Player 2 Won!'), quit()

        #diagonal wins
        if TicTacToe.board[0] == 'X' and TicTacToe.board[4] == 'X' and TicTacToe.board[8] == 'X': print('Player 1 Won!'), quit()
        if TicTacToe.board[2] == 'X' and TicTacToe.board[4] == 'X' and TicTacToe.board[6] == 'X': print('Player 1 Won!'), quit()
        if TicTacToe.board[0] == 'O' and TicTacToe.board[4] == 'O' and TicTacToe.board[8] == 'O': print('Player 2 Won!'), quit()
        if TicTacToe.board[2] == 'O' and TicTacToe.board[4] == 'O' and TicTacToe.board[6] == 'O': print('Player 2 Won!'), quit()

    #takes in an index and checks if the index is equal to x or o and returns true if it is
    def isSpotChosen(self, index):
        index -=1
        if TicTacToe.board[index] == 'X' or TicTacToe.board[index] == 'O':
            return True
        return False
    
    #checks if the board is full
    def isBoardFull(self):
        if not any([True for x in TicTacToe.board if isinstance(x, int)]):
            return True
        return False

    #puts the board on the screen
    def get_board(self):
        for i in range(3):
            print("{} {} {}".format(*TicTacToe.board[3*i:3*i+3]))  
         
TicTacToe()



