import requests


url = 'https://quote.coins.ph/v1/markets'
symbol = "BTC-PHP"

def get_rates():
    response = requests.get(url)
    return filter(lambda x: x["symbol"] == symbol, response.json()["markets"])



if __name__ == '__main__':
    print(get_rates())
