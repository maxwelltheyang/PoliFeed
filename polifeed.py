import requests
def get_headline():
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        'country': 'us',
        'apiKey': '77f3e15e751b42468479f3de9027f77b'
    }
    response = requests.get(base_url, params=params)
    return response.json()

print(get_headline())