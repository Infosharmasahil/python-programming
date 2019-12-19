import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"Eminem"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "7ce5a3383cmshdb8edef6963bba6p1c3470jsn43a3257e68ab"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json() 

#with open ('Eminem.json', 'w') as Eminem_file:
 #   Eminem_file.write(json.dumps(data))


track_list = data['data']

no_of_tracks = len(track_list)
print('Number of tracks {}'.format(no_of_tracks))


print(data.keys())