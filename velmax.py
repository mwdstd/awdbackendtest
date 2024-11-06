import requests
import json
import numpy as np
from models.tkn import get_token
from dataset.surge_max_vel import task, v_ref
import matplotlib.pyplot as plt


tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}


def velmax_plot(task):
    url = 'http://localhost:8000/calc/pooh_max_vel'
    response = requests.post(url, headers=headers, data=json.dumps(task)).json()
    v_vs_md = np.array([[pt['md'], pt['velocity']] for pt in response['graph']])
    plt.figure()
    plt.plot(v_vs_md[:, 0], v_vs_md[:, 1], 'ro-', label='Vmax')
    plt.plot(v_ref[:, 0], v_ref[:, 1], 'g-', label='Vref')
    plt.xlabel('MD, m')
    plt.ylabel('Max drill pipe velocity, m/s')
    plt.legend()
    plt.ylim(bottom=0.)
    plt.show()



velmax_plot(task)