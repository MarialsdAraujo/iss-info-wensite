import urllib.request
import json

def get_weather(lat, lng):
  key = "8a3c8ccaffcc19348b2f06d5ec01a4b2"
  url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={key}&units=metric"

  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  return result