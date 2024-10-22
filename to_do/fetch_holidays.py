import requests
from datetime import datetime

def fetch_holidays(api_key, country_code='GB', year=None):
    """
    Fetches holidays for the given country and year from the Calendarific API.

    Args:
        api_key (str): The API key for authenticating requests to the Calendarific API.
        country_code (str): The country code to fetch holidays for (default is 'GB').
        year (int, optional): The year to fetch holidays for. Defaults to the current year.

    Returns:
        list: A list of holiday dictionaries if the request is successful.
        None: If the API request fails or if no holidays are found.
    """
    if not year:
        year = datetime.now().year  # Use the current year if none is provided

    # Construct the API request URL
    url = f"https://calendarific.com/api/v2/holidays?api_key={api_key}&country={country_code}&year={year}"
    response = requests.get(url)  # Make the GET request to the Calendarific API

    # Debugging: Print out the URL, status code, and full response content for troubleshooting
    print(f"API URL: {url}")  
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code == 200:
        # Return the list of holidays from the JSON response
        holidays = response.json()['response']['holidays']
        return holidays
    else:
        # Return None if the request fails
        return None
