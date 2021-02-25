import json

import requests


def get_from_trello(endpoint: str):
    """
    Make Trello API call and return response deserialized.
    """
    response = requests.request(
        "GET",
        f"https://api.trello.com/1/{endpoint}",
        params={
            'key': '05b4344d198898ec8c78e946cdfb5275',
            'token': '536dc1eaa9af802b23f15e79c91e5465a700ee54ed344f94bc1611ae0b9f005c'
        }
    )
    return json.loads(response.text)
