"""
Module to interact with NASA's Astronomy Picture of the Day (APOD) API.

This module provides a function to fetch the daily astronomy picture and its
associated information from NASA's APOD API. The response includes details
like the title, explanation, and URL of the image.

Configuration:
- NASA_API_KEY: API key required to authenticate requests.
- NASA_API_URL: URL endpoint for NASA's Astronomy Picture of the Day API.
"""

import requests

NASA_API_KEY = "nasa_api_key"
NASA_API_URL = "https://api.nasa.gov/planetary/apod"


def get_nasa_apod():
    """
    Fetch the Astronomy Picture of the Day (APOD) from NASA's API.

    This function makes a request to the NASA API to retrieve the Astronomy Picture of the Day,
    which includes a title, explanation, and a URL to the image or video for the day.

    Returns:
        dict: A dictionary containing the details of the Astronomy Picture of the Day,
              or None if the request fails or the status code is not 200.

    Example:
        {
            "date": "2024-12-15",
            "explanation": "A brief explanation of the image...",
            "title": "Astronomy Picture Title",
            "url": "https://example.com/astronomy-image.jpg"
        }
    """
    try:
        response = requests.get(
            NASA_API_URL, params={"api_key": NASA_API_KEY}, timeout=10
        )
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

    return None
