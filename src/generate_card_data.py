import requests
import json
from time import sleep

# Request a list of all cards release from 2016 onwards (around 23k) and  save them to a .json file.

# url = 'https://api.scryfall.com/cards/search?q=year>%3D2021'
url = 'https://api.scryfall.com/cards/search?q=one+ring&unique=cards&as=grid&order=set'
# save_dir = 'data/cards_after_2021.json'
save_dir = 'data/test.json'

len_data = 0

with open(save_dir, 'w') as fp:
    has_more = True
    while has_more:
        sleep(0.1)
        response = requests.get(url).json()
        print(response)
        has_more = response["has_more"]
        print(has_more)
        data = response["data"]
        print(type(data))
        len_data += len(data)
        json.dump(data, fp)
        if has_more:
            url = response["next_page"]
            print(url)
    
print(f"Saved {len_data} cards to {save_dir}.")
