import json
from urllib.request import urlopen
import pandas as pd
'''jsonFile = open('match_id.json','r')
data = json.load(jsonFile)
csv_data = {'player_name':[], 'player_id':[], 'team_id':[], 'bowling_style':[], 'batting_style':[], 'match_id':[1237181 for i in range(22)],
            'Date':[data['match']['end_date_raw'] for i in range(22)], 'ground_id':[data['match']['ground_id'] for i in range(22)],
            'home_team_id':[data['match']['home_team_id'] for i in range(22)], 'home_team_name':[], 'away_team_id':[0 for i in range(22)], 'away_team_name':[]}
outers = list(data.keys())
centre = data['centre']
for team in data['team']:
    for i in team['player']:
        csv_data['player_name'].append(i['known_as'])
        csv_data['team_id'].append(i['object_id'])
        csv_data['player_id'].append(i['player_id'])
        csv_data['batting_style'].append(i['batting_style'])
        csv_data['bowling_style'].append(i['bowling_style'])
        csv_data['home_team_name'].append(team['team_name'])
        csv_data['away_team_name'].append(team['team_name'])
csv_data['away_team_name'] = list(csv_data['away_team_name'].__reversed__())


for i in csv_data:
    print(csv_data[i])'''

def json_csv(match_id):
    url = 'https://www.espncricinfo.com/matches/engine/match/'+match_id+'.json'
    response = urlopen(url)
    data = json.loads(response.read())

    csv_data = {'match_id': [match_id for i in range(22)],
                'Date': [data['match']['end_date_raw'] for i in range(22)],
                'ground_id': [data['match']['ground_id'] for i in range(22)],
                'home_team_id': [data['match']['home_team_id'] for i in range(22)],
                'home_team_name': [],
                'away_team_id': [data['match']['away_team_id'] for i in range(22)],
                'away_team_name': [],
                'player_name': [], 'player_id': [], 'team_id': [], 'bowling_style': [], 'batting_style': []}
    for team in data['team']:
        for i in team['player']:
            csv_data['player_name'].append(i['known_as'])
            csv_data['team_id'].append(i['object_id'])
            csv_data['player_id'].append(i['player_id'])
            csv_data['batting_style'].append(i['batting_style'])
            csv_data['bowling_style'].append(i['bowling_style'])
            csv_data['home_team_name'].append(team['team_name'])
            csv_data['away_team_name'].append(team['team_name'])
    csv_data['away_team_name'] = list(csv_data['away_team_name'].__reversed__())

    csv_file = pd.DataFrame(csv_data)
    csv_file.to_csv(match_id+'.csv')

id = input('Enter the match ID to get the details -> ')
json_csv(id)



