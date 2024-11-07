import requests
import json
import numpy as np
from models.tkn import get_token
from dataset.holecleaning import task, hcl_ref
import matplotlib.pyplot as plt


tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}


def hole_cleaning_plot(task):
    url = 'http://localhost:8000/calc/holeclean_stat'
    response = requests.post(url, headers=headers, data=json.dumps(task)).json()

    v_ref = np.array([[pt['md'], pt['v_min']] for pt in hcl_ref])
    c_ref = np.array([[pt['md'], pt['c_bed']] for pt in hcl_ref])
    v_cal = np.array([[pt['md'], pt['velocity']] for pt in response['graph']])
    c_cal = np.array([[pt['md'], pt['cuttings']] for pt in response['graph']])

    fig1, ax = plt.subplots()
    ax.plot(v_cal[:, 0], v_cal[:, 1], 'r-')
    ax.plot(v_ref[:, 0], v_ref[:, 1], 'go-')
    ax.set_title('Minimal mud annular velocity')
    ax.set_xlabel('Measured Depth, m')
    ax.set_ylabel('Minimal velocity, m/s')
    # plt.gca().invert_yaxis()

    fig2, ax = plt.subplots()
    ax.plot(c_cal[:, 0], c_cal[:, 1], 'r-')
    ax.plot(c_ref[:, 0], c_ref[:, 1], 'go-')
    ax.set_title('Cutting Bed')
    ax.set_xlabel('Measured Depth, m')
    ax.set_ylabel('Cutting Bed')
    # plt.gca().invert_yaxis()

    plt.show()


hole_cleaning_plot(task)