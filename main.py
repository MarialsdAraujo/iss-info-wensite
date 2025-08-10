from flask import Flask, render_template
from location import get_iss_loc
from country import get_country
from weather import get_weather
from address import get_address
from distance import disc

app = Flask(__name__, static_folder='static')

@app.route("/") # decorator
def index():
    # Get ISS current location
    lat, lng = get_iss_loc()

    # Get address and flag or ocean image
    location_data = get_address(lat, lng)

    # Get full country details (flag, population, region) only if on land
    if location_data['country'] != "Over the ocean":
        # Prefer country code; fallback to name
        query_key = location_data.get('country_code') or location_data.get('country')
        name, region, population, flag_url = get_country(query_key)

        location_data['country_full'] = name
        location_data['region'] = region
        location_data['population'] = population
        location_data['flag'] = flag_url
    else:
        location_data['country_full'] = "Over the ocean"
        location_data['region'] = "N/A"
        location_data['population'] = "N/A"
        location_data['flag'] = "/static/images/ocean.jpg"

    # Get weather under ISS
    weather_data = get_weather(lat, lng)
    try:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
    except:
        temp = "N/A"
        description = "No weather data available"

    # My location
    actual_lat = 43.65107
    actual_lng = -79.347015
    actual_location_name = "Toronto, Canada"
    actual_location_flag = "https://flagcdn.com/w320/ca.png"

    # Calculate distance
    distance_km = disc(actual_lat, actual_lng, lat, lng)

    return render_template("index.html", latitude=lat, longitude=lng, temperature=temp, weather_description=description, location_info=location_data, distance_km=distance_km, actual_location=actual_location_name, actual_location_flag=actual_location_flag)

if __name__ == "__main__": # main is the entry point
    app.run(host="0.0.0.0", port=8080)