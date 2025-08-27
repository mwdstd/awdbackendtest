import requests
import json
from .tkn import get_token, local


base_url = 'https://aide.mwdstd.com/api/calc/'
local_url = 'http://127.0.0.1:8000/calc/'
tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}


def post(endpoint: str, data: dict) -> dict:
    url = f'{base_url}{endpoint}' if not local else f'{local_url}{endpoint}'
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_data = response.json()
    return response_data
