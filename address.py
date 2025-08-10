import urllib.request
import json
import requests
import geopy.distance

def get_address(lat, lng):
    key = "bdc_be66881f7f9d45388f9dfdb3321d63bc"
    url = f"https://api-bdc.net/data/reverse-geocode?latitude={lat}&longitude={lng}&localityLanguage=en&key={key}"

    response = requests.get(url)
    result = response.json()

    country = result.get('countryName', 'Over the ocean')
    country_code = result.get('countryCode', '').upper()
    locality = result.get('locality', 'Unknown')
    city = result.get('city', '')
    label = result.get('location', {}).get('label', '')
    flag_url = "/static/images/ocean.jpg"
    is_ocean = False
  
    if country != "Over the ocean":
        try:
            # Prefer using the alpha code 
            rest_url = f"https://restcountries.com/v3.1/alpha/{country_code}"
            rest_response = requests.get(rest_url)
            rest_data = rest_response.json()

            if isinstance(rest_data, list):
                info = rest_data[0]
            else:
                info = rest_data

            flag_url = info.get('flags', {}).get('png') or info.get('flags', {}).get('svg') or "/static/images/ocean.jpg"

        except Exception as e:
            print(f"Could not retrieve flag: {e}")
            flag_url = "/static/images/ocean.jpg"
    else:
        is_ocean = True

    return {
        'country': country,
        'country_code': country_code,
        'locality': locality,
        'city': city,
        'label': label,
        'flag': flag_url,
        'is_ocean': is_ocean
    }