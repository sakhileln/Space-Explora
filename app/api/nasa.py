"""
Module to interact with NASA's Astronomy Picture of the Day (APOD) API.

This module provides a function to fetch the daily astronomy picture and its
associated information from NASA's APOD API. The response includes details
like the title, explanation, and URL of the image.

Configuration:
- NASA_API_KEY: API key required to authenticate requests.
- NASA_API_URL: URL endpoint for NASA's Astronomy Picture of the Day API.
"""

from .make_api_request import make_api_request

NASA_API_KEY = "nasa_api_key"
NASA_API_URL = "https://api.nasa.gov/planetary/apod"

nasa_data = make_api_request(NASA_API_URL, NASA_API_URL)
