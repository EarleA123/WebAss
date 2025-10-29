# 🚀 Space Bot API Investigation Sheet

**Total Marks: 30**  
**Part 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, and a **Geocoding API** (LocationIQ or Mapbox or other), plus the Python time module.

---

## ✅ Section 1: Webex Messaging API (7 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | `https://webexapis.com/v1/` |
| Authentication Method | `Bearer - Access token` |
| Endpoint to list rooms | `/rooms` |
| Endpoint to get messages | `/messages/{messageId}` |
| Endpoint to send message | `/messages` |
| Required headers | ` list rooms -  "Authorization": "Bearer`
` Get message- "Authorization": "Bearer`
` Send message - "Authorization": "Bearer` |
| Sample full GET or POST request | ` 

url = "https://webexapis.com/v1/rooms"


List Rooms - "items": [
        {
            "id": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZmM4NzE3YjAtYTQzMS0xMWYwLTg0YWMtNDkyNzViOTNmM2Mz",
            "title": "ISS",
            "type": "group",
            "isLocked": false,
            "lastActivity": "2025-10-08T10:31:44.555Z",
            "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zZWIxOGYyMC02ZDdjLTQ4YjQtODJlNy0wZjIzYzA1M2E0Mzk",
            "created": "2025-10-08T10:31:44.555Z",
            "ownerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi83NGY1NzVhZC0zOGRhLTRkN2QtYWE4Ni0wYTNmMDdjYzkwY2Q",
            "isPublic": false,
            "isReadOnly": false
        },
        {
            "id": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNjA5Y2U0NjAtYTQyNy0xMWYwLWFlZDYtOGRhMzQ5YjNmM2Rk",
            "title": "Welcome space",
            "type": "group",
            "isLocked": false,
            "lastActivity": "2025-10-08T09:15:48.486Z",
            "creatorId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zZWIxOGYyMC02ZDdjLTQ4YjQtODJlNy0wZjIzYzA1M2E0Mzk",
            "created": "2025-10-08T09:15:48.006Z",
            "ownerId": "Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi83NGY1NzVhZC0zOGRhLTRkN2QtYWE4Ni0wYTNmMDdjYzkwY2Q",
            "isPublic": false,
            "isReadOnly": false
        }
    ]

https://webexapis.com/v1/messages

Send messages - 

{
    "id": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL01FU1NBR0UvODJiZjc5ZDAtYTlhNS0xMWYwLWI0OTktMzFhNjcxYjhhZTNm",
    "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNDRjNjkxMDAtYTlhNC0xMWYwLWIxOTUtNDFjMDBhYmEyNDNk",
    "roomType": "group",
    "text": "Hello from Postman!",
    "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zZWIxOGYyMC02ZDdjLTQ4YjQtODJlNy0wZjIzYzA1M2E0Mzk",
    "personEmail": "ashleyearles1993@hotmail.com",
    "created": "2025-10-15T09:01:17.677Z"
}

https://webexapis.com/v1/messages/Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL01FU1NBR0UvODJiZjc5ZDAtYTlhNS0xMWYwLWI0OTktMzFhNjcxYjhhZTNm

Get messages - {
    "id": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL01FU1NBR0UvODJiZjc5ZDAtYTlhNS0xMWYwLWI0OTktMzFhNjcxYjhhZTNm",
    "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNDRjNjkxMDAtYTlhNC0xMWYwLWIxOTUtNDFjMDBhYmEyNDNk",
    "roomType": "group",
    "text": "Hello from Postman!",
    "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zZWIxOGYyMC02ZDdjLTQ4YjQtODJlNy0wZjIzYzA1M2E0Mzk",
    "personEmail": "ashleyearles1993@hotmail.com",
    "created": "2025-10-15T09:01:17.677Z"
}



---

## 🛰️ Section 2: ISS Current Location API (3 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | `http://api.open-notify.org` |
| Endpoint for current ISS location | `/iss-now.json` |
| Sample response format (example JSON) |  

{
    "timestamp": 1759315213,
    "message": "success",
    "iss_position": {
        "latitude": "38.2383",
        "longitude": "8.5699"
    }
}
```

```
|

---

## 🗺️ Section 3: Geocoding API (LocationIQ or Mapbox or other) (6 marks)

| Criteria | Details |
|---------|---------|
| Provider used (circle one) | **LocationIQ** |
| API Base URL | `https://us1.locationiq.com` |
| Endpoint for reverse geocoding | `/v1/reverse` |
| Authentication method | `Access Token` |
| Required query parameters | `?key=pk.f8dadac72a6fc03f569c1a0edab8b093&` |
| Sample request with latitude/longitude | `https://us1.locationiq.com/v1/reverse?key=pk.f8dadac72a6fc03f569c1a0edab8b093&lat=51.50344025&lon=-0.12770820958562096&format=json&` |
| Sample JSON response (formatted example) |  
```
{
    "place_id": "274058577",
    "licence": "https://locationiq.com/attribution",
    "osm_type": "relation",
    "osm_id": "1879842",
    "lat": "51.503487750000005",
    "lon": "-0.12769645443243238",
    "display_name": "10 Downing Street, 10, Downing Street, Westminster, Millbank, London, Greater London, England, SW1A 2AA, United Kingdom",
    "address": {
        "government": "10 Downing Street",
        "house_number": "10",
        "road": "Downing Street",
        "quarter": "Westminster",
        "suburb": "Millbank",
        "city": "London",
        "state_district": "Greater London",
        "state": "England",
        "postcode": "SW1A 2AA",
        "country": "United Kingdom",
        "country_code": "gb"
    },
    "boundingbox": [
        "51.5033074",
        "51.5036913",
        "-0.1277991",
        "-0.1273088"
    ]
}

```
|

---

## ⏰ Section 4: Epoch to Human Time Conversion (Python time module) (2 marks)

| Criteria | Details |
|---------|---------|
| Library used | `import time` |
| Function used to convert epoch | `time.ctime()` |
| Sample code to convert timestamp |  
``` 
 import time

timestamp = 734245200  # Example of epoch time calculated in seconds since 1st January 1970
human_time = time.ctime(timestamp)
print(human_time)

```
|
| Output (human-readable time) | ` Thu Apr  8 06:00:00 1993 ` |

---

## 🧩 Section 5: Web Architecture & MVC Design Pattern (12 marks)

### 🌐 Web Architecture – Client-Server Model

- **Client**: The Space Bot Python program. 
- **Server**: The extenal API servers - Webex messaging, LocationIQ and Geocoding API

### 🔁 RESTful API Usage


       Controller    
  ---Space bot python programme---
        - Handles user input
     - Send requests to API's 
 - Co-ordiantes between controller and logic layers.

             

         Model      ---     Handles data: API requests/responses, data processing
 (API Interaction Layer)  

 

 External API Servers                                 View Layer             
   LocationIQ API                                (Webex Messaging API)       
   Geocoding API                               Posts messages to Webex room
   Webex Messaging API              




### 🧠 MVC Pattern in Space Bot

| Component   | Description |
|------------|-------------|
| **Model**  | Space bot python program (Runs locally), webex chatroom  |
| **View**   | Webex messaging API, displays information in the Webex chat when the python program is run  |
| **Controller** | python programme controlls the APIS and feeds the information. |


#### Example:
- Model: 
python program retrieves the ISS location from http://api.open-notify.org/iss-now.json
converts the coodinates into a readable location using LocationIQ
Converts the epoch timestamt use the time function.

- View: 
Webex chat room shows the iss locaton, time and user command

- Controller: 
python logic calls API after getting the initial information from user.
proccesses responses and sends message back to the webex room.


---

### 📝 Notes

- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved them using tools like Postman, Curl, or Python scripts.

---

### ✅ Total: /30