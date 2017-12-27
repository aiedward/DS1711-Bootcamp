# Jiaxin Du 

### the user interface
## input:
##        number of row
##        number of col
##        the first turn that the game wants to start
##        the rule of game (> or <)
##        input a initial game board
## after one turn, it need to input a move as row followed by a space and a column

#input example:
##4
##4
##B
##>
##. . . .
##. B W .
##. W B .
##. . . 

from collections import namedtuple
import othello_class


UserInput = namedtuple("UserInput",
                       ["num_of_row","num_of_col","first_move","rule_of_win"])



def user_interface():
    print("FULL")
    
    ##initial the board and get the input
    input_info = start_input()
    
    initial_board = build_initial_board(input_info.num_of_row)
    
    othello = othello_class.othello(initial_board, input_info.first_move)  #construct the object

    ##show the initial information
    othello.show_discs()
    othello.show_board()

    
    is_valid_move = True
    ## start the game by the first turn
    while True:
        try:
            
            has_valid_move, tail_position_list, valid_move_list = othello.check_valid_move_turn()
  
            if has_valid_move and is_valid_move:
                othello.show_turn()

            if has_valid_move: 
                user_move = ask_for_move()
                is_valid_move = othello.check_valid_move(user_move, valid_move_list) # check valid or not

                if is_valid_move:  # it is a valid move, then go on the game
                    print("VALID")
                    specific_tail_position = othello.get_specific_tail_position(user_move, tail_position_list, valid_move_list)
                    
                    othello.move(user_move, specific_tail_position)
                    othello.show_discs()
                    othello.show_board()
                    
                    ## finish one turn of game
                    ## change the turn
                    othello._turn = othello.opposite_turn()

                elif not is_valid_move:
                    raise othello_class.InvalidMoveError

            
        except othello_class.InvalidMoveError:  ## when the move is invalid
            print("INVALID")


        except othello_class.GameOverError:  ## when the game is over
            othello.show_winner(input_info.rule_of_win)
            break

            
        

    
    
## input functions   
 
def start_input() -> "UserInput":
    '''ask for the row and column for the board and then ask for the first player to move.
        then decide the rule of the game, return a namedtuple with the information
        that the user provide'''
    
    number_of_row = int(input())
    number_of_column = int(input())
    first_move = input()
    rule_of_win = input()
    
    return UserInput(num_of_row = number_of_row,
                     num_of_col = number_of_column,
                     first_move = first_move,
                     rule_of_win = rule_of_win)

    
    
def build_initial_board(num_of_row: int):
    '''ask for the user to input a initial board and
        return the initial board as a 2Dlist'''
    initial_board_list = []
    for row in range(num_of_row):
        content = input().split(" ")
        initial_board_list.append(content)
        
    return initial_board_list

    
    
def ask_for_move() -> tuple:
    '''ask for the user about the move and return that move as a tuple
        (row, col)'''

    move = input().split(" ")
    move_row = int(move[0]) #from top to below
    move_col = int(move[-1]) # from leftmost to rightmost
    
    return (move_row, move_col)
    
    

if __name__ == "__main__":
    user_interface()

    
