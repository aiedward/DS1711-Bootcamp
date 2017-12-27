## Jiaxin Du 

## console-only user interface and one of the two programs's entry points
## play one game of Connect Four using only console interaction.
## The user is repeatedly shown the current state of the game
## with the player's turn and the game board.


import connectfour
import commonfunctions


def user_interface_console():
    '''
    Runs the console-mode user interface from start to finish.
    '''
    current_state = connectfour.new_game()
    commonfunctions.print_board(current_state)


    while True:
        try:
            _game_turn(current_state)
                
            answer = commonfunctions.ask_for_move()
            column_number = commonfunctions.ask_for_column()
            
            current_state = commonfunctions.user_step(current_state, answer, column_number)
            commonfunctions.print_board(current_state)
        except:
            print("You print a invalid number. Please try again.")

        if connectfour.winner(current_state) == 1:
            print("Game over!")
            print("The winner is RED player!")
            break
        elif connectfour.winner(current_state) == 2:
            print("Game over!")
            print("The winner is YELLOW player!")
            break
                



    

## private functions

        

def _game_turn(game_state: connectfour.GameState) -> str:
    """print the correct turn about the game.(red's trun or yellow's turn)"""
    print()
    if game_state.turn == 1:
        print("It is RED player's turn!")
    elif game_state.turn == 2:
        print("It is YELLOW player's turn!")
    print()

    


if __name__ == "__main__":
    user_interface_console()





