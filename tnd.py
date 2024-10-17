import requests
import json
import numpy as np
from models.tkn import get_token
from dataset.tnd_hor_well import task

url = 'http://localhost:8000/calc/tnd'

tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(task)).json()
a = 1