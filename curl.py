## Workaround to overcome shortcomings of FB Python SDK
## Convert cURL requests into python code
## Extract responses as text, load to json/csv 
## Not the absence of importing any FB packages
## Data cleaning / parsing using Pandas
## Resolve token limitation issue
## Breaking Python 3.7 ; run in 3.6/3,5 

import requests
import json
import csv
import pandas
import pandas as pd 
from pandas.io.json import json_normalize
import pprint

## Specify fields, access token, and other parameters
'''
params = (
    ('fields', 'id,name'),
    ('access_token', 'EAAE8mDZAuUOABAFCAK3XP0Iz5rUGLWFUzeCQXGVqsMAlaZCiXZAsLvUrzSkWNtXQZBeNAcLxuhJrkjAjzrYPoHqMpZCxzYDoQFOHT87omyZCqRrqS6vh2mp21C9mbzZChovEOzFoDZBPHfeYpo0jFt79Ch0p9T3Qd6UVxhGMwCok0uGtu7Q1Y4ZAHix6ZAmjw7MWQpJfzvtyGzlAZDZD'),
)
'''

params = (
    ('fields', 'id,name,about'),
    ('access_token', 'EAAE8mDZAuUOABABhaf8q3eXHRRbHhd7sUv4uyfrw0rxnQiWFNn5JNwZCwkwHFGiknimWK3rFIHhZAbuZAKD2F4FePNT5ZCWetnqMCPazESVGQ6m57YHQQtIAIzGiRiH3do3AIHbkm6FYIzLMhOer1WyHg32NdMlnnBXdZAbkhc6PqGZALGGwblOAm9kU6dGZB3G8zGyLEMa1VQZDZD'),
)

## Use GET method from requests package:
response = requests.get('https://graph.facebook.com/v3.2/me', params=params)

## Transform <RESPONSE 200> into text:
answer = response.text
print(response.text) 

## Save GET request as JSON:
## Need to write function that looks less hacky: 

extract = json.loads(answer)

with open('fb.json', 'w') as outfile:
    json.dump(extract, outfile)

## JSON-to-csv conversion (currently breaks Python 3.7 )

#master = pd.read_json('fb.json', lines=True)
master = pd.read_json('fb.json')
master_json_raw = pd.read_json('fb.json', lines=True)
master_json = master_json_raw.apply(lambda x: pd.Series([x[0]['id'],x[0]['name'], x[0]['about']]), axis = 1)

master_json.columns=['Account ID', 'Account Name', 'About']

#export as csv
master_json.to_csv('master.csv')

print(master_json)

df = pd.read_json(master, orient='columns')
df = pd.DataFrame.from_dict(json_normalize(master), orient='columns')

with open('fb.json') as f:
    data = json.load(f)

pprint(data)