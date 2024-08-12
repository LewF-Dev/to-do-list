import requests
from datetime import datetime

def fetch_holidays(api_key, country_code='GB', year=None):
    if not year:
        year = datetime.now().year
    
    url = f"https://calendarific.com/api/v2/holidays?api_key={api_key}&country={country_code}&year={year}"
    response = requests.get(url)
    
    print(f"API URL: {url}")  # This will show the API URL being used
    print(f"Response Status Code: {response.status_code}")  # This will show the response status code
    print(f"Response Content: {response.content}")  # This will show the full response content

    if response.status_code == 200:
        holidays = response.json()['response']['holidays']
        return holidays
    else:
        return None
