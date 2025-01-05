"""
Module to make HTTP requests to an API.

This module provides a utility function, `make_api_request`, which can be used to
send GET requests to an API endpoint. It handles optional API keys, query parameters,
timeouts, and error handling.

Functions:
    make_api_request(url, api_key: str = None): Sends a GET request to the specified URL
    and returns the response in JSON format if the request is successful.
    Handles timeouts and request exceptions.
"""

import requests


def make_api_request(url, api_key: str = None):
    """
    Send a GET request to the specified URL with optional API key and query parameters.

    This function sends a GET request to the given URL, including an optional API key
    as a query parameter. It handles timeouts, request exceptions, and checks for a
    successful response (HTTP status code 200). If successful, it returns the response
    data in JSON format.

    Args:
        url (str): The API endpoint URL to send the GET request to.
        api_key (str, optional): The API key to authenticate the request. Defaults to None.

    Returns:
        dict or None: The response data in JSON format if the request is successful,
                      or None if the request fails or encounters an error.
    """
    try:
        # Include the API key in the query parameters, if provided
        params = {}
        if api_key:
            params["api_key"] = api_key

        # Send the request with query parameters and a timeout
        response = requests.get(url, params=params, timeout=10)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return None


def parse_mission_data(api_response):
    """
    Parse API response and ensure all required fields are present.
    """
    missions = []
    for mission in api_response:
        name = mission.get("mission_name")
        status = mission.get("launch_success")
        description = mission.get("details", "No description available.")
        if name is None or status is None:
            continue  # Skip missions with missing critical fields

        missions.append(
            {
                "name": name,
                "status": "Success" if status else "Failure",
                "description": description,
            }
        )
    return missions
