import requests
import json
import time
from iso3166 import countries

choice = input("Do you want to use the hard-coded access token? (y/n)? ") #choice to let the user choose if they want to use hardcoded key or their own

if choice.lower() == "n":
    accessToken = input("Please enter your access token: ")
    accessToken = "Bearer " + accessToken  
else:
    accessToken = "Bearer MDI3OWUxN2MtYTVmZS00ZmYwLWI0MWMtZmNlY2MxNzQ3NTI0ZmY1M2JhMjctMWMx_PE93_74f575ad-38da-4d7d-aa86-0a3f07cc90cd"

r = requests.get(
    "https://webexapis.com/v1/rooms",
    headers={"Authorization": accessToken} # using r as a variable this is getting checking get request to webex with the access token
    )

if r.status_code != 200:
    raise Exception(f"Webex API error. Status code: {r.status_code}. Response: {r.text}") # Making sure the reponse is 200 meaning it was succesful

print("\nList of available rooms:")
rooms = r.json()["items"]
for room in rooms:
    print(f"{room['type'].capitalize()} - {room['title']}") # listing the available rooms in the webex messagnger

#-----------------------------------------------------#
    
while True:
    roomNameToSearch = input("Which room should be monitored for the /seconds messages? ")
    roomIdToGetMessages = None # letting the user choose what room they wish to use for the get and post requests

    for room in rooms:
        if room["title"].find(roomNameToSearch) != -1:
            print("Found rooms with the word " + roomNameToSearch)
            print(room["title"])
            roomIdToGetMessages = room["id"]
            roomTitleToGetMessages = room["title"]
            print("Found room: " + roomTitleToGetMessages)
            break #making sure the room requested from user is within the webex rooms

    if roomIdToGetMessages is None:
        print("Sorry, I didn't find any room with " + roomNameToSearch + " in it.")
        print("Please try again...")
    else:
        break

#-----------------------------------------------------#

while True:
    time.sleep(1)
    GetParameters = {
        "roomId": roomIdToGetMessages,
        "max": 1
    } # this tells the code how often to check the webex room for messages, currently set to 1 second

    
    r = requests.get(
        "https://webexapis.com/v1/messages",
        params=GetParameters,
        headers={"Authorization": accessToken} # same get request to get the message desplayed in the room by user - looking for a /5 for example
    )

    
    if not r.status_code == 200: #status code check again with exception if not 200
        raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))

    json_data = r.json()
    if len(json_data["items"]) == 0:
        print("No messages found in this room yet.")
        continue

    messages = json_data["items"]
    message = messages[0]["text"]
    print("Latest message:", message) #variable created to print the latest message in the python screen

    if message.lower().startswith("/next "): #Only if the message displayed is /next will the program go down this if statement
        city_query = message[6:].strip() #message [6:] removes the first 6 letters of the string in this case '/next ' , strip() removes any leading or trailing spaces from the word.
        if not city_query:
            print("Usage: /next [city name]")
            continue 

        print(f"Looking up ISS pass time for: {city_query}") 

        
        mapsAPIGetParameters = {
            "key": "pk.f8dadac72a6fc03f569c1a0edab8b093",
            "q": city_query,
            "format": "json",
            "limit": 1
        } #IPlocation json being put into a variable as a list.

        r = requests.get("https://us1.locationiq.com/v1/search", params=mapsAPIGetParameters)
        if r.status_code != 200 or "error" in r.text.lower():
            responseMessage = f"Could not find coordinates for '{city_query}'."
        else:
            data = r.json()[0]
            lat = float(data["lat"])
            lon = float(data["lon"])
            print(f"Using coordinates: lat={lat}, lon={lon}") #if statement checking the satus code of the request and an else statement if it fails

            
            N2YOApiKey = "QHMN4Q-4B2P4M-D86DVW-5LGF"  #N2YO is a api that allows us to track where the ISS is going to be.
            N2yoUrl = f"https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/{lat}/{lon}/0/3/10/&apiKey={N2YOApiKey}"

            r = requests.get(N2yoUrl) #sending the request to N2YO
            if r.status_code == 200: #Status code reposne from API
                data = r.json()
                if "passes" in data and len(data["passes"]) > 0: #Checking json for work passes to use for formatting
                    next_pass = data["passes"][0] #passes is set at next past to be transfered into a time
                    risetime = time.ctime(next_pass["startUTC"])#variable set as a readable time format for the pass time of that location
                    duration = next_pass["duration"] // 60 #Setting a variable to display for the duration the ISS will fly over that location
                    

                    responseMessage = ( #Layout for the response message
                        f"The ISS will next pass over **{city_query.title()}** "
                        f"on {risetime} for about {duration} minutes)."
                    )
                else:
                    responseMessage = f"No visible ISS passes over {city_query.title()} in the next 3 days." # response if the ISS isnt flying over that location in the next 3 days
            else:
                print("N2YO API error:", r.text)
                responseMessage = "Could not retrieve ISS pass data. Try again later." #error or fail message if all other statements are not met.

        
        HTTPHeaders = {"Authorization": accessToken, "Content-Type": "application/json"} #webex room post request data
        PostData = {"roomId": roomIdToGetMessages, "text": responseMessage}

        r = requests.post("https://webexapis.com/v1/messages", data=json.dumps(PostData), headers=HTTPHeaders) #posting the data to webex
        if r.status_code == 200: #returns status code for user.
            print("Next pass info sent to Webex.")
        else:
            print("Error posting to Webex:", r.text)

        continue

    
    if message.find("/") == 0: 
        if (message[1:].isdigit()):
            seconds = int(message[1:])
        else:
            print("Invalid command. Use format /seconds (e.g. /5)")
            continue # checking that the webex room is desplaying the correct format message, this will not continue until a /+intager is desplayed

        
        if seconds > 5:
            seconds = 5 # just making the /intager into 5 seconds if the user inputs something higher. this is for efficiency

        time.sleep(seconds) #tells the code to wait the amount of seconds before actioning the next code

        
        r = requests.get("http://api.open-notify.org/iss-now.json") # gets request for the ISS location

        json_data = r.json() #setting the json data recieved into a variable

        if not r.status_code == 200: #status check with error
            print("Error retrieving ISS data:", r.text)
            continue

        
        lat = json_data["iss_position"]["latitude"]
        lng = json_data["iss_position"]["longitude"]
        timestamp = json_data["timestamp"] # formatting the json data into variables to send to locationIQ api

        timeString = time.ctime(timestamp) #converting the json timestamp into a user friendly date format

        
        mapsAPIGetParameters = {
        "key": "pk.f8dadac72a6fc03f569c1a0edab8b093",
        "lat": lat,
        "lon": lng,
        "format": "json" # formatting perameters into a variable to send to the locationIQ api
        }

        
        r = requests.get("https://us1.locationiq.com/v1/reverse", params=mapsAPIGetParameters)

        
        if r.status_code != 200 or "error" in r.text.lower(): #status code for locationIQ
            print("LocationIQ could not geocode this location (probably over water).")
            print("Response:", r.text)
            CountryResult = "XZ"  
            StateResult = ""    # if response is succesful but locationIQ does not have a reverse geocode for the
            CityResult = ""     # location then that means its flying over water, so instead of getting a error message i have formatted it
            StreetResult = ""   # to display a message saying that its probably over water.
        else:
            
            json_data = r.json()
            address = json_data.get("address", {}) # if successful this formats the json response from LocationIQ into variable ready to post to the webex room

            CountryResult = address.get("country_code", "XZ").upper()
            StateResult = address.get("state", "")
            CityResult = address.get("city", address.get("town", address.get("village", "")))
            StreetResult = address.get("road", "")



        
        if not CountryResult == "XZ":
            CountryResult = countries.get(CountryResult).name #this is using iso3166 to format the country result into its proper user readable name

        
        if CountryResult == "XZ":
            responseMessage = f"On {timeString}, the ISS was flying over a body of water at latitude {lat}° and longitude {lng}°."
        elif CityResult and StateResult:
            responseMessage = f"In {CityResult}, {StateResult} the ISS flew over on {timeString}.\nCoordinates: ({lat}°, {lng}°)"
        else:
            responseMessage = f"On {timeString}, the ISS was flying over {CountryResult} at coordinates ({lat}°, {lng}°)." #last part of formatting depending on the response

        
        print("Sending to Webex: " + responseMessage) # last message in python window before posting reponse

        HTTPHeaders = {
            "Authorization": accessToken,
            "Content-Type": "application/json" #post response type
        }

        PostData = {
            "roomId": roomIdToGetMessages, #where to post the response, will be the same room that the user chose earlier
            "text": responseMessage
        }

        r = requests.post( #posting the response
            "https://webexapis.com/v1/messages",
            data=json.dumps(PostData),
            headers=HTTPHeaders
        )

        if not r.status_code == 200: #checking the status code of response with error message if unsuccesful
            print("Error posting to Webex:", r.text)
        else:
            print("Message successfully sent to Webex room.")
            break #breaks the loop to stop the program once the response has been posted.
