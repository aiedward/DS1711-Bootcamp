## Jiaxin Du

## I32CFSP and all socket handling

## inculde functions that implement the ICS 32
## Connect Four Server protocol using sockets




import socket
from collections import namedtuple

CfConnection = namedtuple('CfConnection',
                          ['socket','input','output'])



WELCOME = 0
READY = 1
OKAY = 2
INVALID = 3
WINNER_RED = 4
WINNER_YELLOW = 5


class ConnectFourError(Exception):
    pass





_SHOW_DEBUG_TRACE = False


def connect(host: str, port: int) -> "CfConenction":
    '''
    Connects to aserver running on the given host and listening
    on the given port, returning a CfConnection object describing
    that connection if successful, or raising an exception if the attempt
    to connect fails.
    '''
    
    cf_socket = socket.socket()
    print("Connecting to {} ...".format(host))
    cf_socket.connect((host, port))
    print("Connect! ")
    
    cf_socket_input = cf_socket.makefile('r')
    cf_socket_output = cf_socket.makefile('w')

    return CfConnection(socket = cf_socket,
                        input = cf_socket_input,
                        output = cf_socket_output)



def hello(connection: CfConnection, username: str) -> WELCOME:
    '''
    Logs a user into the service over a previously-made connection.
    If the attempt to send text to the server or receive a response
    fails (or if the server sends back a response that does not conform to
    the protocol), an exception is raised.
    '''
    
    _write_line(connection, 'I32CFSP_HELLO '+ username)

    response = _read_line(connection)

    if response == "WELCOME "+username:
        
        return WELCOME
    else:
        raise ConnectFourError()



def start(connection: CfConnection) -> READY:
    """
    Start with the artifical intellgence.If the attempt to send text
    to the server or receive a response fails, an exception is raised.
    Else, return a value if READY
    """

    _write_line(connection, "AI_GAME")

    response = _read_line(connection)

    if response == "READY":
        return READY
    else:
        raise ConnectFourError()



def drop(connection: CfConnection, column_number: int) -> "info":
    """ ask for the move about drop and return the specific value"""

    _write_line(connection, "DROP " + str(column_number))
    response = _read_line(connection)

    info = _handle_command(connection, response)
    return info
    
   

def pop(connection: CfConnection, column_number: int) -> "info":
    """ ask for the move about drop and return the specific value"""

    _write_line(connection, "POP " + str(column_number))
    response = _read_line(connection)

    info = _handle_command(connection, response)
    return info



def close(connection: CfConnection) -> None:
    """close the connection to the server"""
    connection.input.close()
    connection.output.close()
    connection.socket.close()
    







# Private Functions

def _write_line(connection: CfConnection, line: str)-> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence, and ensures that it is sent immediately.
    '''
    connection.output.write(line + '\r\n')
    connection.output.flush()

    if _SHOW_DEBUG_TRACE:
        print("SENT: " + line)


def _read_line(connection: CfConnection)->str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''
    line = connection.input.readline()[:-1]
    
    if _SHOW_DEBUG_TRACE:
        print("RCVD: "+ line)
        
    return line


def _handle_command(connection: CfConnection, response:str) -> tuple or INVALID or WINNER_RED or WINNER_YELLOW:
    """return the different responses by different command"""

    if response == "OKAY":
        ai_info = _read_line(connection).split()
        
        ai_move = ai_info[0].lower()
        ai_column = ai_info[-1]

        line = _read_line(connection)

        if line == "READY":
            return OKAY, ai_move, ai_column
        
        elif line == "WINNER_YELLOW":
            return WINNER_YELLOW, ai_move, ai_column
        
        else:
            raise ConnectFourError()
    
    elif response == "INVALID":
        line = _read_line(connection)
        return INVALID

    elif response == "WINNER_RED":
        return WINNER_RED

    elif response == "WINNER_YELLOW":
        return WINNER_YELLOW

    else:
        raise ConnectFourError()   
