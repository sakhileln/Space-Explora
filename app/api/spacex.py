import requests

SPACE_API_URL = "https://api.spacexdata.com/v4/launches"

def get_spacex_launches():
    response = requests.get(SPACE_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None