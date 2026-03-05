import requests
import json
from time import sleep

# Request a list of all cards release from 2016 onwards (around 23k) and  save them to a .json file.

url = 'https://api.scryfall.com/cards/search?q=year>%3D2016'
save_dir = 'data/cards_after_2016.json'

len_data = 0

with open(save_dir, 'w') as fp:
    has_more = True
    while has_more:
        sleep(0.2)
        response = requests.get(url)
        has_more = response.json()["has_more"]
        print(has_more)
        len_data += len(response.json()["data"])
        json.dump(response.json()["data"], fp)
        if has_more:
            url = response.json()["next_page"]
            print(url)
    
print(f"Saved {len_data} cards to {save_dir}.")
