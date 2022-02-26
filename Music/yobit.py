import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    resource = requests.get(url).json()
    price = resource['ticker']['last']
    return str(price) + 'usd'

