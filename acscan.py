import requests
import json
import numpy as np
from models.tkn import get_token
from dataset.iscwsa_ac_r4 import task

url = 'http://localhost:8000/calc/acscan'

tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(task)).json()
a = 1