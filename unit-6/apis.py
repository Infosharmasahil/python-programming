#use the requests module
import requests
import json

#response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

data = response.json()
#pretty print the result
#print(data)
#print(json.dumps(data, indent =4))

#print(data.keys()) #look at the keys on your data object

#look at the teams object -check the type
##print(type(data['teams']))

#look at the first item in this list
#print(data['teams'][0])

#pretty print
#print(json.dumps(data['teams'][0], indent =4))

#save to a file

with open ('nhl.json', 'w') as nhl_file:
    nhl_file.write(json.dumps(data))

print("done....")