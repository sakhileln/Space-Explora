"""
This module provides functions for interacting with the SpaceX Launch API.

It includes functionality to fetch information about SpaceX launches using
the public SpaceX data API. The API returns a list of launches, including
details like launch dates, mission names, and more.
"""

from .make_api_request import make_api_request

SPACEX_API_URL = "https://api.spacexdata.com/v4/launches"

spacex_data = make_api_request(SPACEX_API_URL)
