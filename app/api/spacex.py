"""
This module provides functions for interacting with the SpaceX Launch API.

It includes functionality to fetch information about SpaceX launches using
the public SpaceX data API. The API returns a list of launches, including
details like launch dates, mission names, and more.
"""

import requests

SPACE_API_URL = "https://api.spacexdata.com/v4/launches"


def get_spacex_launches():
    """
    Fetch a list of SpaceX launches from the SpaceX public API.

    This function sends a GET request to the SpaceX Launch API endpoint
    and returns a list of launch data in JSON format. Each launch object
    contains details about the launch, such as the mission name, date, and
    other relevant information.

    Returns:
        list: A list of dictionaries where each dictionary represents a SpaceX launch.
              If the request fails or the status code is not 200, None is returned.
    """
    try:
        response = requests.get(SPACE_API_URL, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")

    return None
