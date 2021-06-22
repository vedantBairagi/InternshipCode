import json
from urllib.request import urlopen
import pandas as pd
match_ids = ['1216538', '1237178', '1216536', '1216537', '1216494', '1237180', '1216546', '1216507', '1216527', '1216510', '1216504', '1216500', '1216524', '1216513', '1216502', '1216511', '1216535', '1216547', '1216506', '1216505', '1237177', '1237181', '1216516', '1216521', '1216499', '1216534', '1216533', '1216542', '1216541', '1216531', '1216545', '1216522', '1216520', '1216525', '1216530', '1216501', '1216523', '1216492', '1216544', '1216529', '1216496', '1216515', '1216532', '1216509', '1216503', '1216508', '1216543', '1216526', '1216539', '1216498', '1216540', '1216497', '1216495', '1216512', '1216493', '1216518', '1216514', '1216528', '1216517', '1216519']
'''url = 'https://www.espncricinfo.com/matches/engine/match/1216494.json'
response = urlopen(url)

data = json.loads(response.read())
csv_data = {'player_name':[], 'player_id':[], 'team_id':[], 'bowling_style':[], 'batting_style':[], 'match_id':[1237181 for i in range(22)],
            'Date':[data['match']['end_date_raw'] for i in range(22)], 'ground_id':[data['match']['ground_id'] for i in range(22)],
            'home_team_id':[data['match']['home_team_id'] for i in range(22)], 'home_team_name':[], 'away_team_id':[0 for i in range(22)], 'away_team_name':[]}
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
    print(csv_data[i])
'''
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
    csv_file.to_csv('All_matches/'+match_id+'.csv')

for id in match_ids:
    json_csv(id)





