# Jiaxin Du 

## implements the various outputs 
## each kind of output must be implemented as a separate Class


## same name, same parameters, same type of return value




class steps:
    def __init__(self):
        self._direction =""
    

    
    def print_result(self, result) -> str:
        """ take a result, and print a message and print steps """
        
        print("\nDIRECTIONS")
        for leg in result["route"]["legs"]:
            for maneuver in leg["maneuvers"]:
                print(maneuver["narrative"])
        
        


class totaldistance:
    def __init__(self):
        self._distance = 0

    def set_data(self, result) -> int:
        """
        take the result, and return self by changing the distance
        """
        
        return self
        
        
    def print_result(self, result) -> str:
        """ take a result, and print a message about the total distance"""
        for leg in result["route"]["legs"]:
            for maneuver in leg["maneuvers"]:
                self._distance += maneuver["distance"]
        print("\nTOTAL DISTANCE: {} miles".format(round(self._distance)))  # miles
        
        



class totaltime:
    def __init__(self):
        self._time = 0


        
        
    def print_result(self, result) -> str:
        """take a result, and print a message about the total time"""
        for leg in result["route"]["legs"]:
            for maneuver in leg["maneuvers"]:
                self._time += maneuver["time"]
    
        print("\nTOTAL TIME: {} minutes".format(round(self._time/60))) ##minute





class latlong:
    def __init__(self):
        self._latitude = 0
        self._longitude = 0
        self._collection = []
        
     
        
    
    def get_lat(self, latitude) -> str:
        """ add N or S according the different latitude"""
        if float(latitude) > 0:
            self._latitude = latitude + "N"
        elif float(latitude) < 0:
            self._latitude = latitude[1:] + "S"
        
        return self._latitude
            

    
    def get_long(self, longitude) -> str:
        """ add W or E according the different longitude"""
        if float(longitude) > 0:
            self._longitude = longitude + "E"
        elif float(longitude) < 0:
            self._longitude = longitude[1:] + "W"
            
        return self._longitude
        

        
    def get_collection(self, result) -> list:
        """return a collection of latitude and longitude in order to build elevation url"""
        for location in result["route"]["locations"]:
            self._latitude = location["latLng"]["lat"]
            self._longitude = location["latLng"]["lng"]

            latlng = "{},{}".format(self._latitude, self._longitude)
            self._collection.append(latlng)

        return self._collection

        
        
    def print_result(self, result) -> str:
        """take a result, and print a message and print latitude, longitude"""
        print("\nLATLONGS")
        for location in result["route"]["locations"]:     
            
            self._latitude = self.get_lat("{:5.2f}".format(location["latLng"]["lat"]))
            self._longitude = self.get_long("{:6.2f}".format(location["latLng"]["lng"]))
       
            print(self._latitude, self._longitude)
            
            
           




class elevation:
    def __init__(self):
        self._elevation = 0

        
        
    def print_result(self, result) -> str:
        """ take a result and print a message and print elevation"""
        print("\nELEVATIONS")
        for elevation_result in result:
            for elevation in elevation_result["elevationProfile"]:
                self._elevation = elevation["height"]
                
                print(round(self._elevation*3.28))#*3.28  # feet
            
            
    













