import requests

API_KEY = '33027bcd'  # Coloque aqui sua chave da OMDb API
BASE_URL = 'http://www.omdbapi.com/'

def GetPieceByID(imdb_id) -> dict:
    params = {
        'apikey': API_KEY,
        'i': imdb_id
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if data.get('Response') == 'False':
        return {'error': 'Not Found'}
    
    return data

def GetPieceByTitle(title) -> dict:
    params = {
        'apikey': API_KEY,
        's': title
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get('Response') == 'False':
        return {'error': 'Not Found'}

    return data