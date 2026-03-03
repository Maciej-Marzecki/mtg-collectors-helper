import requests
import json
from currency_converter import CurrencyConverter

url = 'https://api.scryfall.com/cards/search?order=cmc&q=one+ring'

# A GET request to the API
response = requests.get(url)

# Print the response
# print(json.dumps(response.json(), indent=4))

# get price in EUR
price_eur = response.json()["data"][0]["prices"]["eur"]
print(f"Current Skateboard's price in EUR is {price_eur}")

# convert price from EUR to PLN
c = CurrencyConverter()
price_pln = round(c.convert(float(price_eur), 'EUR', 'PLN'), 2)
print(f"and current Skateboard's price in PLN is {price_pln}")
