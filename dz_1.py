import requests
import json
r = requests.get('https://api.github.com/users/nojio4ka/repos')
with open('../data.json', 'w') as f:
    json.dump(r.json(), f)

for i in r.json():
    print(i['name'])