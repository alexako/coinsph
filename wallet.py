import requests
import _hmac


url = "https://coins.ph/api/v3/crypto-accounts/"

def get_wallet():
    nonce = _hmac.get_nonce()
    signature = _hmac.sign_request(url, nonce)

    headers = {
        'ACCESS_SIGNATURE': signature,
        'ACCESS_KEY': _hmac.API_KEY,
        'ACCESS_NONCE': nonce,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    return response.json()


if __name__ == '__main__':
    print(get_wallet())

