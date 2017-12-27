## Jiaxin Du 


## ConnectFour for the network 
## user interface for the networked version of the game
## that plays against an artifical intelligence by connecting to a server

## REMINDER: it only can work with the uci network
## host: woodhouse.ics.uci.edu
## port: 4444

import cfsocket
import commonfunctions
import connectfour




def user_interface_network()->None:
    '''
    Runs the console-mode user interface from start to finish.
    '''
    game_state = connectfour.new_game()
    _show_welcome_banner()
    
    while True:  ## host and port
        try:
            host = read_host()
            port = read_port()
            connection = cfsocket.connect(host, port)         
            print()
            break

        except:
            print()
            print("Invalid. Connect fail. Program ended.")
            return


    try:
        while True:  ## username
            username = _ask_for_username()
            print()
            try:
                response = cfsocket.hello(connection, username)

                if response == cfsocket.WELCOME:
                    break
                else:
                    raise cfsocket.ConnectFourError()
            except cfsocket.ConnectFourError:
                print("You print a wrong port.")
                return
                

        while True:  ## start game with artifical intellgence
            response = cfsocket.start(connection)

            if response == cfsocket.READY:
                break
            else:
                raise cfsocket.ConnectFourError()
            
        play_game(connection, game_state) ## drop or pop


    finally:
        cfsocket.close(connection)
        print("Goodbye!")



                
def read_host() -> str:
    '''
    Asks the user to specify what host they'd like to connect to,
    continuing to ask until a valid answer is given.  An answer is
    considered valid when it consists of something other than just
    spaces.
    '''

    while True:
        host = input('Host: ').strip()

        if host == '':
            print('Please specify a host (either a name or an IP address)')
        else:
            return host



def read_port() -> int:
    '''
    Asks the user to specify what port they'd like to connect to,
    continuing to ask until a valid answer is given.  A port must be an
    integer between 0 and 65535.
    '''

    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')





def play_game(connection: cfsocket.CfConnection, game_state):
    '''
    play the game with the different response:
    if response is winner_red, break and print the winner.
    if response is winner_yellow, break and print the winner.
    if response is invalid, try it again until a valid number is given.
    if response is okay, then play game with artifical intellgence.
    '''
    while True:

        answer = commonfunctions.ask_for_move()
        column_number = commonfunctions.ask_for_column()


        try:
            game_state = commonfunctions.user_step(game_state, answer, column_number)
        except:
            pass            
        response = _drop_or_pop(connection, answer, column_number)

        if response == cfsocket.WINNER_RED:
            commonfunctions.print_board(game_state)
            
            print("Congratulation!")
            print("The winner is Red. You are win!")
            break


        elif response == cfsocket.INVALID:
            print("You print an invalid number." + "\n" + "Please try again"+"\n")
            

        try:    
            if response[0] == cfsocket.WINNER_YELLOW:
                game_state = _ai_step(connection,game_state,response)
                commonfunctions.print_board(game_state)
                
                print("The winner is Yellow!")
                break
            
            elif response[0] == cfsocket.OKAY:
                game_state = _ai_step(connection,game_state,response)

        except TypeError:
            if response == cfsocket.WINNER_YELLOW:
                
                print("The winner is Yellow!")
                break               

        commonfunctions.print_board(game_state)







def _ai_step(connection: cfsocket.CfConnection,game_state: connectfour.GameState, response: tuple)-> "game_state":
    """ return a new game state with artifical intellgence's move of drop or pop"""
    ai_move = response[1]
    ai_column = response[-1]

    if ai_move == "drop":
        game_state = connectfour.drop(game_state,int(ai_column)-1)

    elif ai_move == "pop":
        game_state = connectfour.pop(game_state,int(ai_column)-1)

    return game_state    




def _drop_or_pop(connection: cfsocket.CfConnection, answer:str, column_number: int) -> int:
    """determine the movement about drop or pop with the input and return the response,drop or pop"""
    if answer.startswith("d"):
        response = cfsocket.drop(connection, column_number+1)
    elif answer.startswith("p"):
        response = cfsocket.pop(connection, column_number +1)

    return response
        



def _show_welcome_banner() -> None:
    """shows the welcome banner"""
    print("Welcome to the connectfour client!")
    print()
    print("Please play game with your username.")
    print()




def _ask_for_username() -> str:
    """
    ask for the user's name.
    If there is a whitespace, then ask again until a vaild username is given.
    If it is invalid ask again until a vaild username is given
    """
    while True:
        username = input("Username: ").strip()

        if " " in username:
            print("There is a whitespace in your username.Please print again.")
        elif len(username)>0:
            return username
        else:
            print("That username is blank; please try again.")

    


if __name__ == "__main__":
    user_interface_network()


    
