import requests
import json
import time

choice = input("Do you want to use the hard-coded access token? (y/n)? ")

if choice.lower() == "n":
    accessToken = input("Please enter your access token: ")
    accessToken = "Bearer " + accessToken  
else:
    accessToken = "Bearer YmQ4MWRiNjMtYmMzYS00NGI3LWI0NDEtN2VmM2U0NDRlNmIzYTY0NTY4NDMtNTRj_PE93_74f575ad-38da-4d7d-aa86-0a3f07cc90cd"

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

