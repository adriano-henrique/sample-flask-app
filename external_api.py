import requests
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
api_key = os.getenv('OPENWEATHER_API_KEY')

def get_city_info(city):
    request_url = f"{BASE_URL}?q={city}&appid={api_key}"
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json(), response.status_code
    except requests.exceptions.HTTPError as http_err:
        return {"error": "HTTP error occurred", "details": str(http_err)}, response.status_code
    except requests.exceptions.ConnectionError as conn_err:
        return {"error": "Connection error occurred", "details": str(conn_err)}, 503
    except requests.exceptions.Timeout as timeout_err:
        return {"error": "Timeout error occurred", "details": str(timeout_err)}, 504
    except requests.exceptions.RequestException as req_err:
        return {"error": "An error occurred", "details": str(req_err)}, 500

get_city_info("London")