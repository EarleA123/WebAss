import requests
import json
import time

choice = input("Do you want to use the hard-coded access token? (y/n)? ")

if choice.lower() == "n":
    accessToken = input("Please enter your access token: ")
    accessToken = "Bearer " + accessToken  
else:
    accessToken = "Bearer ZDBjMmJiZjktNmNjOC00M2ZhLTk0OWQtMjhjNGM5Y2NmMWExN2E5NDI2YmEtY2U2_PE93_74f575ad-38da-4d7d-aa86-0a3f07cc90cd"

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

