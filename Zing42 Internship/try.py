import json
jsonFile = open('match_id.json','r')
data = json.load(jsonFile)
print(data['match']['ground_id'])
print(data['match']['end_date_raw'])
print(data['match'])

for team in data['team']:
    for i in team['player']:

