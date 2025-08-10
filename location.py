import urllib.request, requests
import json

def get_iss_loc():
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    data = response.json()

    # lat and lng are the keys in the dictionary that we want to access
    lat = data["iss_position"]["latitude"]
    lng = data["iss_position"]["longitude"]

    print(f"https://www.google.com/maps/place/{lat}+{lng}")
    print(f"The ISS is currently at longitude: {lng} and latitude: {lat}")

    return float(lat), float(lng)  # we use float to convert the string to a number and return it as a tuple
