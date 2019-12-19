import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"Cardi B"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "7ce5a3383cmshdb8edef6963bba6p1c3470jsn43a3257e68ab"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json() 

with open ('CardiB.json', 'w') as CardiB_file:
    CardiB_file.write(json.dumps(data))