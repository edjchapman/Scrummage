import json

import requests

from scrummage.settings import TRELLO_KEY, TRELLO_TOKEN


def get_from_trello(endpoint: str):
    """
    Make Trello API call and return response deserialized.
    """
    response = requests.request(
        "GET",
        f"https://api.trello.com/1/{endpoint}",
        params={
            'key': TRELLO_KEY,
            'token': TRELLO_TOKEN
        }
    )
    return json.loads(response.text)
