# Jiaxin Du

## interacts with the Open MapQuest APLs
## building URLs
## making HTTP request   
## parsing JSON response



import json
import urllib.parse
import urllib.request
import various_outputs

BASE_MAPQUEST_URL = "http://open.mapquestapi.com/"
APL_KEY = "mNWeAZGB1OlmeQA1PgeQ7TEzqLoP9JZj"


##example:  http://open.mapquestapi.com/directions/v2/route?
##            key=APIKEY&from=Irvine%2CCA&to=Los+Angeles%2CCA



def build_route_url(locations: list) -> str:
   '''
   This function takes a location list, and builds and returns a URL that can be used to ask the
   route url
   '''
   request_parameters = _get_route_parameters(locations)
   
   route_url = BASE_MAPQUEST_URL + "directions/v2" + "/route?" + urllib.parse.urlencode(request_parameters)

   return route_url

  



##example: "http://open.mapquestapi.com/elevation/v1/profile?\
##         key=mNWeAZGB1OlmeQA1PgeQ7TEzqLoP9JZj&shapeFormat=raw&\
##         latLngCollection=39.74012,-104.9849,39.7995,-105.7237,39.6404,-106.3736"



def build_elevation_url(route_result:dict, location_list: list) -> str:
   '''
   This function takes a location list and the result about the route ur,
   and builds and returns a URL that can be used to ask the
   elevation url
   '''
   elevation_urls = []
   latLng = various_outputs.latlong()

   for num in range(len(location_list)):
      request_parameters = [("key", APL_KEY),
                           ("latLngCollection", latLng.get_collection(route_result)[num])]
    
   
      elevation_url = BASE_MAPQUEST_URL + "elevation/v1" + "/profile?" +\
                      urllib.parse.urlencode(request_parameters)
                     
      elevation_urls.append(elevation_url)

   return elevation_urls



    
def get_result(url: str) -> dict:
   '''
   This function takes a URL and returns a Python dictionary representing the
   parsed JSON response.(route_result)
   '''
   response = None
   try:
      response = urllib.request.urlopen(url)
      json_text = response.read().decode("utf-8")

      return json.loads(json_text)
   finally:
      if response != None:
         response.close()





def get_elevation_result(url:list) -> [dict]:
   '''
   This function takes a URL and returns a Python dictionary representing the
   parsed JSON response.(elevation_result)
   '''

   elevation_results = []
   
   for elevation_url in url:
      elevation_results.append(get_result(elevation_url))
      
   return elevation_results
      


## private functions

def _get_route_parameters(location_list: list) -> list:
   """
   This function takes a locaiton list, and return the request parameters
   """
   
   request_parameters = [("key", APL_KEY),("from", location_list[0])]
   for num in range(len(location_list)-1):
       request_parameters.append(("to", location_list[num+1]))
        
   return request_parameters





