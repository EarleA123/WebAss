import requests
import json
import time
from iso3166 import countries

choice = input("Do you want to use the hard-coded access token? (y/n)? ")

if choice.lower() == "n":
    accessToken = input("Please enter your access token: ")
    accessToken = "Bearer " + accessToken  
else:
    accessToken = "Bearer NDNjNjg3ODQtNjkyMS00MTk1LThiZWItY2E3M2Q2ODJiMDQxZjU2YzE5NTUtNDk4_PE93_74f575ad-38da-4d7d-aa86-0a3f07cc90cd"

r = requests.get(
    "https://webexapis.com/v1/rooms",
    headers={"Authorization": accessToken}
    )

if r.status_code != 200:
    raise Exception(f"Webex API error. Status code: {r.status_code}. Response: {r.text}")

print("\nList of available rooms:")
rooms = r.json()["items"]
for room in rooms:
    print(f"{room['type'].capitalize()} - {room['title']}")

#-----------------------------------------------------#
    
while True:
    roomNameToSearch = input("Which room should be monitored for the /seconds messages? ")
    roomIdToGetMessages = None

    for room in rooms:
        if room["title"].find(roomNameToSearch) != -1:
            print("Found rooms with the word " + roomNameToSearch)
            print(room["title"])
            roomIdToGetMessages = room["id"]
            roomTitleToGetMessages = room["title"]
            print("Found room: " + roomTitleToGetMessages)
            break

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
    }

    
    r = requests.get(
        "https://webexapis.com/v1/messages",
        params=GetParameters,
        headers={"Authorization": accessToken}
    )

    
    if not r.status_code == 200:
        raise Exception("Incorrect reply from Webex API. Status code: {}. Text: {}".format(r.status_code, r.text))

    json_data = r.json()
    if len(json_data["items"]) == 0:
        print("No messages found in this room yet.")
        continue

    messages = json_data["items"]
    message = messages[0]["text"]
    print("Latest message:", message)

    if message.find("/") == 0:
        if (message[1:].isdigit()):
            seconds = int(message[1:])
        else:
            print("Invalid command. Use format /seconds (e.g. /5)")
            continue

        
        if seconds > 5:
            seconds = 5

        time.sleep(seconds)

        
        r = requests.get("http://api.open-notify.org/iss-now.json")

        json_data = r.json()

        if not r.status_code == 200:
            print("Error retrieving ISS data:", r.text)
            continue

        
        lat = json_data["iss_position"]["latitude"]
        lng = json_data["iss_position"]["longitude"]
        timestamp = json_data["timestamp"]

        timeString = time.ctime(timestamp)

        
        mapsAPIGetParameters = {
        "key": "pk.f8dadac72a6fc03f569c1a0edab8b093",
        "lat": lat,
        "lon": lng,
        "format": "json"
        }

        
        r = requests.get("https://us1.locationiq.com/v1/reverse", params=mapsAPIGetParameters)

        
        if r.status_code != 200 or "error" in r.text.lower():
            print("LocationIQ could not geocode this location (probably over water).")
            print("Response:", r.text)
            CountryResult = "XZ"  
            StateResult = ""
            CityResult = ""
            StreetResult = ""
        else:
            
            json_data = r.json()
            address = json_data.get("address", {})

            CountryResult = address.get("country_code", "XZ").upper()
            StateResult = address.get("state", "")
            CityResult = address.get("city", address.get("town", address.get("village", "")))
            StreetResult = address.get("road", "")

            CountryResult = locationInfo["adminArea1"]
            StateResult = locationInfo["adminArea3"]
            CityResult = locationInfo["adminArea5"]
            StreetResult = locationInfo["street"]

        
        if not CountryResult == "XZ":
            CountryResult = countries.get(CountryResult).name

        
        if CountryResult == "XZ":
            responseMessage = f"On {timeString}, the ISS was flying over a body of water at latitude {lat}° and longitude {lng}°."
        elif CityResult and StateResult:
            responseMessage = f"In {CityResult}, {StateResult} the ISS flew over on {timeString}.\nCoordinates: ({lat}°, {lng}°)"
        else:
            responseMessage = f"On {timeString}, the ISS was flying over {CountryResult} at coordinates ({lat}°, {lng}°)."

        
        print("Sending to Webex: " + responseMessage)

        HTTPHeaders = {
            "Authorization": accessToken,
            "Content-Type": "application/json"
        }

        PostData = {
            "roomId": roomIdToGetMessages,
            "text": responseMessage
        }

        r = requests.post(
            "https://webexapis.com/v1/messages",
            data=json.dumps(PostData),
            headers=HTTPHeaders
        )

        if not r.status_code == 200:
            print("Error posting to Webex:", r.text)
        else:
            print("Message successfully sent to Webex room.")
