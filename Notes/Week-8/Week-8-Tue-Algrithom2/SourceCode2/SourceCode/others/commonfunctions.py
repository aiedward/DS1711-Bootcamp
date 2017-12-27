## Jiaxin Du 

## same functions in both user interfaces
## (ConnectFourConsole and ConnectFourNetwork)

import connectfour



def print_board(game_state: connectfour.GameState) -> None:
    """print a board with a given gamestate 7*6 (seven columns and six rows)"""

    new_list = _convert_sign(game_state.board)
    
    print()
    for num in range(connectfour.BOARD_COLUMNS):
        print(num+1, end = " " )
    print()
    
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            print(new_list[col][row], end = " ")
        print()

    print()





def user_step(game_state:connectfour.GameState, command:str, column_number:int) -> connectfour.GameState:    
    '''return a new game state with the movement of the user(d or p).'''

    if command == "d":
        game_state = connectfour.drop(game_state, column_number)
           
    elif command == "p":
        game_state = connectfour.pop(game_state, column_number)

    else:
        raise TypeError
    
    return game_state





def ask_for_move() -> str:
    """
    ask for the movement(only d or p).
    If invalid try again until a valid movement is given.
    """
    while True:
        command = input("Drop or Pop?(d or p) ").strip().lower()

        if command != "d" and command != "p":
            print("You print an invalid one. Please print again.(d or p)")
        else:
            return command



def ask_for_column() -> int:
    """
    ask for the column, a number between 1 and 7.
    if invalid try again until a valid column number is given
    """
    while True:

        try:
            column = int(input("Which column?(1-7) "))
            if column > 0 and column <= 7:
                
                return column-1
            else:
                print("You print an invaild number. Please print a number between 1 and 7.")
        
        except:
            print("You print an invaild number. Please print a number between 1 and 7.")




##  private functions


def _convert_sign(game_list: [[int]]) -> [[str]]:
    """translate the specific number in 2D list to a specific str in 2D list."""

    board = []
    for row in range(len(game_list)):
        temp = []
        for col in range(len(game_list[row])):
            
            if game_list[row][col] == 0:
                temp.append(".")

            elif game_list[row][col] == 1:
                temp.append("R")

            elif game_list[row][col] == 2:
                temp.append("Y")
                
        board.append(temp)

    return board


