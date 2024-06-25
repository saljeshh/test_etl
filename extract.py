import requests


def extract():
    """
    Extracts data from API and returns data 
    
    """
    response = requests.get(f'https://yts.mx/api/v2/list_movies.json?limit=50&page=1')
    
    data = response.json()
     
    return data