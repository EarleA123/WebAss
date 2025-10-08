import requests

url = "https://webexapis.com/v1/rooms"

payload = None

headers = {
    "Authorization": "Bearer ZTY4ZGU2NjctNDYyZS00Njk2LThmNzYtZTM0MDhmMWU0YWQ3ZTFkNGM1NWMtMTI0_PE93_74f575ad-38da-4d7d-aa86-0a3f07cc90cd",
    "Accept": "application/json"
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))

