import requests
import time
import json
from requests.structures import CaseInsensitiveDict

def unsplash_keywords():

    key_words = [
        'face', 'man', 'woman', 'lady', 'lass', 'lad', 'boy' 'girl', 
        'child', 'baby', 'hombre', 'senor', 'senorita', 'mujer', 
        'fraulein', 'frau', 'dama', 'grossvater', 'malchik', 'babe', 
        'master', 'bonita', 'chica', 'abuela', 'black man', 'white man', 
        'asian man', 'old man', 'old woman', 'happy girl outdoor', 'sad person', 
        'black baby', 'black girl', 'black woman', 'happy baby', 'queen', 
        'ugly girl', 'ugly boy', 'little boy', 'little girl', 'chinese lady', 'dirty boy',
        'asian woman'
        ]
    i = 0
    page = 1
    while True:
        url = f"https://api.unsplash.com/search/photos?query={key_words[i]}&client_id=2JKak5ISr4dbnKOWvZM3FUi0fRVnqTCqVsA5uYsMcB8&per_page=30&page={page}"
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = "Bearer {token}"
        resp = requests.get(url, headers=headers)
        our_json = json.loads(resp.text)
        with open(f'{key_words[i]}.txt', 'a') as pt:
            pt.write("%s\n" % our_json)
        page+=1
        # time.sleep(72)

unsplash_keywords()