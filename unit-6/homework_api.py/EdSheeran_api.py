import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"Ed Sheeran"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "7ce5a3383cmshdb8edef6963bba6p1c3470jsn43a3257e68ab"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json() 

with open ('EdSheeran.json', 'w') as EdSheeran_file:
    EdSheeran_file.write(json.dumps(data))
