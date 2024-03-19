import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_headline():
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        'country': 'us',
        'apiKey': API_KEY
    }
    response = requests.get(base_url, params=params)
    return response.json()

print(get_headline())