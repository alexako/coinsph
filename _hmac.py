import hashlib
import hmac
import time
import json
import os


API_KEY = os.environ["COINS_KEY"]
API_SECRET = os.environ["COINS_SECRET"]


def get_nonce():
    """ Return a nonce based on the current time.

    A nonce should only use once and shoud always
    be increasing.
    Using the current time is perfect for this.
    """

    return int(time.time() * 1e6)

def sign_request(url, nonce, body=None):
    " Return an HMAC signature based on the request. "

    if body is None:
        message = str(nonce) + url
    else:
        body = json.dumps(body, separators=(',', ':'))
        message = str(nonce) + url + body

    return str(
        hmac.new(
            str(API_SECRET),
            message,
            hashlib.sha256
            ).hexdigest()
        )
