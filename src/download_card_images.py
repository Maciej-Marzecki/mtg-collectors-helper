import requests
import json
from time import sleep
from pathlib import Path
 

# Request a list of all cards release from 2021 onwards (around 19k) and downloads their images to data folder.
next_url = 'https://api.scryfall.com/cards/search?q=year>%3D2021'

img_counter = 0

# If the number of requested cards exceeds 175 scryfall API sends the data in batches.
# To check if there is more batches left look for boolean "has_more", if True - there are more requsts needed.
has_more = True
while has_more:
    sleep(0.1)  # Scryfalls Rate Limits and Good Citizenship rule
    response = requests.get(next_url).json()
    has_more = response["has_more"]
    # count all cards in current batch for statistics
    total = len(response["data"])

    for card in response["data"]:
        # get basic card info, to identify a MTG card you need at least set name and collector number
        card_name = card["name"]
        card_set = card["set"]
        card_collectors_number = card["collector_number"]
        img_counter += 1

        # in case of an image missing for card - skip it
        if card["image_status"] == "missing":
            continue

        # in case of a double sided card get only the front side image
        try:
            card_image_url = card["image_uris"]["normal"]
        except:
            card_image_url = card["card_faces"][0]["image_uris"]["normal"] # For double sided cards

        # download the card and save it to the data folder with an identifiable name
        image_path = Path(f"data/{card_set}_{card_collectors_number}.jpg")
        if not image_path.is_file():
            with open(image_path, "wb") as file:
                print(f"{img_counter}. Name: {card_name}, Set: {card_set}, Num: {card_collectors_number}")
                sleep(0.1)  # Scryfalls Rate Limits and Good Citizenship rule
                img_response = requests.get(card_image_url)
                file.write(img_response.content)
        else:
            # if card was already downloaded into the data folder - skip it
            print(f"{img_counter}. Skipped")

    # if there is more batches to download - get the url of next batch
    if has_more:
            next_url = response["next_page"]
