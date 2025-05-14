import requests

# open-notify.org
api_url = 'http://api.open-notify.org/astros.json'


response = requests.get(api_url)
json = response.json()
print('The people currently in space are:')
for person in json['people']:
    print(person['name'], ' (', person['craft'], ')', sep='')