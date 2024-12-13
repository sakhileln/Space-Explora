import requests

NASA_API_KEY = "nasa_api_key"
NASA_API_URL = "https://api.nasa.gov/planetary/apod"


def get_nasa_apod():
    response = requests.get(NASA_API_URL, params={"api_key": NASA_API_KEY})
    if response.status_code == 200:
        return response.json()
    else:
        return None
