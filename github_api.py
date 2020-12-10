import requests
from repository import Repository

def get_top_repo():
    params = {
        'since' : 'daily',
        'language_spoken' : 'English'
    }
    result = requests.get('https://hackertab.pupubird.com/repositories',params= params)
    return Repository(result.json()[0])