import requests
import json
import numpy as np
from models.tkn import get_token
from dataset.ac_iscwsa_r4 import task, ac_benchmark
from models.ac import plot_osf

url = 'http://localhost:8000/calc/acscan'

tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}

def acscan_plot(task, case_id):
    response = requests.post(url, headers=headers, data=json.dumps(task)).json()
    osf_calc = np.array([[pt['depth1'], pt['osf']] for pt in response['scan']])
    osf_bnch = np.array([[pt['md'], pt['osf']] for pt in ac_benchmark])
    plot_osf(osf_calc, osf_bnch, case_id)

acscan_plot(task, 'ISCWSA offset well #3')