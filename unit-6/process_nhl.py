import json

with open('nhl.json', 'r') as nhl_file:
    data = json.load(nhl_file)

print(data.keys())

#how many teams are in the nhl

team_count = len(data['teams'])

print(team_count)

'''
    if team not in team_total_count.keys():
        team_total_count[team_count] = []
        team_total_count[team_count].append(team)

print(team_total_count)

   def team_count():
       return (team[team.valuefor team
       data['team_count'].value()
'''
eastern_conf_teams = []
oldest_year = '2019'
oldest_name = ''
#when was the boston bruins started

for team in data['teams']:
    if team['name'] == 'Boston Bruins':
        print(team ['firstYearOfPlay'])


#what is the oldest team in the nhl
     if team['firstYearOfPlay'] < oldest_year:
         oldest_year = team['firstYearOfPlay']
         oldest_name = team['name']


#what are the teams in the eastern conference

     if team['conference']['name'] == 'Eastern' :
         eastern_conf_teams.append(team['name'])

print('Eastern conference teams: ', end= ' ')
print(eastern_conf_teams)

print('Oldest team is {}, started in {}'.format(oldest_name, oldest_year))

