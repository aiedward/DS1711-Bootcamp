# Jiaxin Du 

## Project 3 

## reads the input and constructs the objects that wil
## generate the program's output

## input:   the number of the locations that the user wants to get
##          the locaiton name
##          ......
##          the numebr of the kinds of the outputs that the user wants to get
##          kinds of input
##          ......

#input example:
##3
##4533 Campus Dr, Irvine, CA
##1111 Figueroa St, Los Angeles, CA
##3799 S Las Vegas Blvd, Las Vegas, NV
##5
##LATLONG
##STEPS
##TOTALTIME
##TOTALDISTANCE
##ELEVATION

from collections import namedtuple
import interact_apls
import various_outputs



UserInput = namedtuple("UserInput",
                       ["number_of_location", "location_list", \
                       "number_of_output", "output_list"])


def user_interface() -> None:
    check = True
    try:
        
        inputs = start_input() ##read the input
        
        location_list = inputs.location_list
        output_list  = inputs.output_list

        route_url = interact_apls.build_route_url(location_list)
        route_result = interact_apls.get_result(route_url)
        

        check = check_error(route_result) ##check if the route can be found

        if check:
                
            elevation_urls = interact_apls.build_elevation_url(route_result, location_list)
            elevation_results = interact_apls.get_elevation_result(elevation_urls)
        

            
            handle_command_class(output_list, route_result, elevation_results) ##construct object and generate outputs  

    except:
        print("\nMAPQUEST ERROR")






def start_input() -> "Userinput":
    """
    This function reads the input, return a namedtuple named
    UserInput with number_of_location, location_list, number_of_outputs, output_list
    """
    location_list = []
    output_list = []
    

    number_of_location = int(input())

    for num in range(number_of_location):
        location_list.append(input())


    number_of_output = int(input())

    for num in range(number_of_output):
        output_list.append(input())


    return UserInput(number_of_location = number_of_location,
                     location_list = location_list,
                     number_of_output = number_of_output,
                     output_list = output_list)



            
        


        
def check_error(route_result) -> bool:
    """
    This function takes the route result, and check if the route
    can be found by MapQuest, if not break and print the message,else continue
    """
    
    status_code = route_result["info"]["statuscode"]
    if status_code == 400:
        print("\nNO ROUTE FOUND")
        check = False
    else:
        check = True
    return check

        

## kind {STEPS, TOTALDISTANCE, TOTALTIME, LATLONG, ELEVATION}


def handle_command_class(output_list , route_result, elevation_results) -> str:
    """
    This function takes the output list and route and elevation result, and
    construct the different objects and set their data and then print the result
    that the user wants
    """

    output_dict = {"STEPS": various_outputs.steps(), "TOTALTIME": various_outputs.totaltime(),
                   "TOTALDISTANCE": various_outputs.totaldistance(), "LATLONG": various_outputs.latlong(),
                   "ELEVATION": various_outputs.elevation()}
    for kind in output_list:
        kind_object = output_dict[kind]

        if kind != "ELEVATION":
            kind_object.print_result(route_result)

        elif kind == "ELEVATION":
            kind_object.print_result(elevation_results)
      
    print("\nDirections Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.")



if __name__ == "__main__":
    user_interface()  

    
