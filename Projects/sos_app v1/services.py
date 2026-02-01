import requests

from space import space

class Services:
    
    #This is how we can access the Google Maps and Google Geolocation API using this API key
    
    def __init__(self): 
        self.gmaps_key = "Your GMAPS API KEY"

    #This is where the GeoLocation API comes to locate the user using their coordinates.

    def get_location(self): 
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={self.gmaps_key}"
        response = requests.post(url)
        data = response.json()

        if "location" in data: 
            lat = data["location"]["lat"]
            lng = data["location"]["lng"]
            return f"{lat},{lng}"
        
        #if the User's Location is not identifiable for some reason this will be printed
        
        else: 
            print("⚠️ Could not detect location:", data)
            return None
        
     #This is where the location is passed to locate the diffrent places that we want to search -- "Hospitals"
    
    def get_places(self, location, place_type):
        url = (
            f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
            f"location={location}&radius=5000&type={place_type.lower()}&key={self.gmaps_key}"
        )
        response = requests.get(url)
        data = response.json()
        
        #if the data does not got anything or if theres an error this conditional will run and will be printed when you execute the program.
        
        if data.get("status") != "OK":
            print(f"Google Maps API Error: {data.get('status')}")
            print("Error message:", data.get("error_message", "No error message provided"))
            
            return []

        return data.get("results", [])

    def text_search(self, query):
        url = (
            f"https://maps.googleapis.com/maps/api/place/textsearch/json?"
            f"query={query}&key={self.gmaps_key}"
        )
        response = requests.get(url)
        data = response.json()
        
        #if the data does not got anything or if theres an error this conditional will run and will be printed when you execute the program.
        
        if data.get("status") != "OK":
            print(f"Google Maps API Error: {data.get('status')}")
            print("Error message:", data.get("error_message", "No error message provided"))
            return []

        return data.get("results", [])




