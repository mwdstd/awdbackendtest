import requests
import json
from tkn import get_token
from dataset.iscwsa import iscwsa1, iscwsa3
from models.ac import EouTrajectory

url = 'http://localhost:8000/calc/wellunc'

tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(iscwsa3))
traj = EouTrajectory.model_validate(response.json())
