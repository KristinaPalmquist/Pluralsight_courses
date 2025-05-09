import requests

api_key = '9a69fce6bfc44077800110711250905'
location = 'Orlando'
api_url = 'http://api.weatherapi.com/v1/current.json?key=' + api_key + '&q=' + location + '&aqi=no'
response = requests.get(api_url)
weather_json = response.json()

current = weather_json.get('current')
temp_c = current.get('temp_c')
temp_f = current.get('temp_f')
condition = current.get('condition')
description = weather_json.get('current').get('condition').get('text')

print(f'The current temperature in {location} is {temp_c} C = {temp_f} F and the weather is {description}')


# json_format = {
#     "current": {
#         "temp_c": 21.7,
#         "temp_f": 71.1,
#         "condition": {
#             "text": "Partly Cloudy",
#             "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
#             "code": 1003
#         },
#     }
#     }