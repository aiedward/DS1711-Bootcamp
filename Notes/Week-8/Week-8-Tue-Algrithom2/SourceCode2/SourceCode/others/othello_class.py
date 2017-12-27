# Jiaxin Du 

### game logic
### a class named othello

class InvalidMoveError(Exception):
    pass


class GameOverError(Exception):
    pass



class othello:
    def __init__(self, game_board, first_move):
        self._gamestate = game_board
        
        self._white = "W"
        self._black = "B"
        self._none = "."
        
        self._whitenum = 0
        self._blacknum = 0
        
        self._turn = first_move

        
        
    def show_board(self):
        '''print the game board'''

        for row in self._gamestate:
            for col in row:
                print(col, end = " ")
            print()
                
                
    
    def show_discs(self):
        '''print the two player's number of discs'''
        self._whitenum = 0
        self._blacknum = 0
        
        for row in self._gamestate:
            for col in row:
                if col == self._white:
                    self._whitenum += 1
                elif col == self._black:
                    self._blacknum += 1
                
        print("B: {}  W: {}".format(self._blacknum, self._whitenum))
    



    def show_turn(self):
        '''print the current turn'''
        
        print("TURN: {}".format(self._turn))




    def show_winner(self, rule_of_win):
        '''when the game is over, according to the rule of game,
            print the winner at the end'''
        
        if rule_of_win == ">":
            # choose the winner with the more discses on the board
            if self._whitenum > self._blacknum:
                winner = self._white
            elif self._blacknum > self._whitenum:
                winner = self._black
            else:
                winner = "NONE"

        elif rule_of_win == "<":
            if self._whitenum < self._blacknum:
                winner = self._white
            elif self._blacknum < self._whitenum:
                winner = self._black
            else:
                winner = "NONE"

        print("WINNER: {}".format(winner))


    
    def opposite_turn(self):
        '''change the turn of the game'''

        if self._turn == self._white:
            self._turn =  self._black
        else:
            self._turn = self._white

        return self._turn




    def get_tail_position_list(self) -> [tuple]:
        """get a list with all the discs on the board current turn's color"""
        tail_position_list = []  # white turn
        
   
        for row in range(len(self._gamestate)):
            for col in range(len(self._gamestate[row])): # [0,0]
                
                if self._gamestate[row][col] == self._turn: # white
                    tail_position_list.append((row+1, col+1))

        return tail_position_list





    def get_head_position_list(self, tail_position_list) -> [tuple]:
        '''return a list with all possible valid move for current turn'''
        head_position_list = []  ## valid move position
        
        # tail_position is (0,0)  original
        possible_move_direction = [(-1,-1),(-1,0),(-1,1),
                                   (0,-1),(0,1),
                                   (1,-1),(1,0),(1,1)]
        
        for row, col in tail_position_list:
            possible_move = []
            row = row - 1
            col = col - 1

            for change_x, change_y in possible_move_direction:
                change_row = row + change_x
                change_col = col + change_y               
                change_times = 0         
                
                
                while True:
                    try:
                        change_position = self._gamestate[change_row][change_col]
                    except IndexError:
                        break
                    

                    if change_times == 0 and change_position == self._none:
                        break


                    elif change_position == self._turn:                       
                        break
                    

                    elif change_position != self._none and change_position != self._turn:                        

                        if change_x >= 0:
                            if change_row < 0 or change_row > len(self._gamestate)-1:
                                break
                            else:
                                change_row += change_x
                                
                        elif change_x < 0:
                            if change_row <= 0 or change_row > len(self._gamestate)-1:
                                break
                            else:
                                change_row += change_x


                        if change_y >= 0:
                            if change_col < 0 or change_col > len(self._gamestate[0])-1:
                                break
                            else:
                                change_col += change_y
                        elif change_y < 0:
                            if change_col <= 0 or change_col > len(self._gamestate[0])-1:
                                break
                            else:
                                change_col += change_y
                                

                        change_times += 1

                    elif change_times > 0 and change_position == self._none:
                        possible_move.append((change_row+1, change_col+1))
                        break

            head_position_list.append(possible_move)
    
                
        return head_position_list






   
    def get_specific_tail_position(self, user_move, tail_position_list, valid_move_list) -> list:
        '''return a list of the specific tail position according to the move'''
        
        specific_tail_position = []


        for order in range(len(valid_move_list)):
            for valid_move in valid_move_list[order]:
                
                if user_move == valid_move:
                    # it is a valid move
                    tail_position = tail_position_list[order]
                    specific_tail_position.append(tail_position)


        return specific_tail_position




                 



    def check_valid_move_turn(self):
        ''' if there is a valid on that current turn, return a bool about has a valid move
            and a tail position list and a valid move list.
            if there is no valid move, change the turn and check if that turn has a valid move,
            then change for that turn.
            If two turns both have no valid move, then raise the game over error'''


        has_valid_move = True

        tail_position_list = self.get_tail_position_list()
        valid_move_list = self.get_head_position_list(tail_position_list)

        if valid_move_list.count([]) == len(valid_move_list):  ## empty
            self._turn = self.opposite_turn()
            has_valid_move = False

            tail_position_list = self.get_tail_position_list()
            valid_move_list = self.get_head_position_list(tail_position_list)

            if valid_move_list.count([]) == len(valid_move_list):  ## empty again
                raise GameOverError()
            
        return has_valid_move, tail_position_list, valid_move_list




    def check_valid_move(self, user_move, valid_move_list) -> bool:
        ''' take the user the user move and the valid move list, and
            return a bool about is valid move or not'''
        is_valid_move = False
        for sublist in valid_move_list:
            for valid_move in sublist:
                if user_move == valid_move:
                    is_valid_move = True

        return is_valid_move
                
        



    def move(self, move, tail_position_list):
        '''according to the user move and the tail position, change the discs on the board'''
        move_row, move_col = move

        for tail_row, tail_col in tail_position_list:            
            
            if tail_row == move_row:
                for change_col in range(min(tail_col,move_col)-1,max(tail_col, move_col)):
                    self._gamestate[move_row-1][change_col] = self._turn
            
            
            elif tail_col == move_col:
                for change_row in range(min(tail_row, move_row)-1,max(tail_row, move_row)):
                    self._gamestate[change_row][move_col-1] = self._turn
    
            #(3,1) (5,3)  minis change(4,2)
            # (1,1) (3,3)
            elif (tail_row - tail_col == move_row - move_col):
                change_row = min(tail_row, move_row)-1
                change_col = min(tail_col, move_col)-1  
                             
                while True:
                    self._gamestate[change_row][change_col] = self._turn            
                
                    change_row += 1
                    change_col += 1
                    if change_row == max(tail_row, move_row):
                        break

            # (4,1) (2,3) add change(3,2)==(2,1)-->(1,2)   
            elif (tail_row + tail_col == move_row + move_col):
                change_row = max(tail_row, move_row)-1
                change_col = min(tail_col, move_col)-1
                
                while True:
                    self._gamestate[change_row][change_col] = self._turn            
                
                    change_row -= 1
                    change_col += 1
                    if change_col == max(tail_col, move_col):
                        break




