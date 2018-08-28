
import json
import turtle
import urllib.request
import time
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
lat = location['latitude']
long = location['longitude']
print('latitude: ',lat)
print('long: ',long)
screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.jpg')
screen.register_shape('iss2.png')
iss = turtle.Turtle()
iss.shape('iss2.png')
iss.setheading(90)

iss.penup()
iss.goto(long,lat)
lat = 29.5502
lon = -95.007
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url =  'http://api.open-notify.org/iss-pass.json'
url = url + '?lon='+str(lon)+'&lat='+str(lat)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
over = result['response'][1]['risetime']
style = ('Arial', 6 ,'bold')
location.write(time.ctime(over) , font=style)
