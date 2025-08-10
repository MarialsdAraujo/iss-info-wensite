import urllib.request
import requests
import json

import requests

def get_country(country_code):
    try:
        url = f"https://restcountries.com/v3.1/alpha/{country_code}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        info = data[0] if isinstance(data, list) else data  # some responses return a dict

        name = info['name']['common']
        region = info.get('region', 'Unknown')
        population = info.get('population', 'Unknown')
        flags = info.get('flags', {})
        flag_url = flags.get('png') or flags.get('svg') or None

        return name, region, population, flag_url

    except (KeyError, TypeError, IndexError):
        return "Unknown country (not in API)", 'None', 'None', None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return "Unknown country (not in API)", 'None', 'None', None