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

List Rooms - {"items": [
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
}

Send message - { "message": "The request could not be understood by the server due to malformed syntax.",
    "errors": [
        {
            "description": "The request could not be understood by the server due to malformed syntax."
        }
    ],
    "trackingId": "ROUTERGW_9821ff86-98e1-4c18-98d0-4e35fce54c7b"
}

Get message - {
    "message": "The requested resource could not be found.",
    "errors": [
        {
            "description": "The requested resource could not be found."
        }
    ],
    "trackingId": "ROUTERGW_6c23d103-81f0-47f0-9549-7df90f5f3286"
}






` |

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
| Sample request with latitude/longitude | `lat=51.50344025&lon=-0.12770820958562096&format=json` |
| Sample JSON response (formatted example) |  
```
{
    "place_id": "399379424",
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
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |  
```  
```
|
| Output (human-readable time) | `_______________________________` |

---

## 🧩 Section 5: Web Architecture & MVC Design Pattern (12 marks)

### 🌐 Web Architecture – Client-Server Model

- **Client**: 
- **Server**: 
- (Explain the communication between them & include a block diagram )

### 🔁 RESTful API Usage

- 
- 
- 

### 🧠 MVC Pattern in Space Bot

| Component   | Description |
|------------|-------------|
| **Model**  |  |
| **View**   |  |
| **Controller** |  |


#### Example:
- Model: 
- View: 
- Controller: 

---

### 📝 Notes

- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com or Mapbox, open-notify.org or other ISS API).
- Be prepared to explain your findings to your instructor or demo how you retrieved them using tools like Postman, Curl, or Python scripts.

---

### ✅ Total: /30