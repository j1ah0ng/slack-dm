import json
import requests

token = 'YOUR-TOKEN'

r = requests.get('https://slack.com/api/users.list?token=' + token + '&pretty=1')

with open('raw.json', 'w', encoding='utf-8') as outfile:
    json.dump(r.json(), outfile)

with open('raw.json') as f:
    data = json.load(f)

with open('users.txt', 'w', encoding='utf-8') as u:

    for member in data['members']:
        if not member['deleted'] and not member['is_bot']:
            if 'first_name' in member['profile'].keys():
                json.dump({'user_id': member['id'],
                          'user_name': member['name'],
                          'first_name': member['profile']['first_name'
                          ]}, u)
                u.write('\n')
            else:

                json.dump({'user_id': member['id'],
                          'user_name': member['name'], 'first_name': ''
                          }, u)
                u.write('\n')

print('users.txt generated')
