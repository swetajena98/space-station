#!/bin/python3

import json
import turtle
import urllib.request
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print('people in space: ',result['number'])
people = result['people']
for p in people:
 print(p['name'])
