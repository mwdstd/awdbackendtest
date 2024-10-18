import requests
import json
import matplotlib.pyplot as plt
from models.tkn import get_token
from dataset.tnd_hor_well import task, drillmech

url = 'http://localhost:8000/calc/tnd'

tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}

def tnd_plot(task):
    response = requests.post(url, headers=headers, data=json.dumps(task)).json()
    block_weight = 37  # tons

    dpt = [pnt['md'] for pnt in response]
    so = [pnt['dragRih'] + block_weight for pnt in response]
    pu = [pnt['dragPoh'] + block_weight for pnt in response]
    ro = [pnt['dragRot'] + block_weight for pnt in response]
    tq = [pnt['torque'] / 1000 for pnt in response]

    dpt_msr = [pnt['md'] for pnt in drillmech]
    so_msr = [pnt['so'] for pnt in drillmech]
    pu_msr = [pnt['pu'] for pnt in drillmech]
    ro_msr = [pnt['rot'] for pnt in drillmech]
    tq_msr = [pnt['tq'] for pnt in drillmech]

    fig1, ax = plt.subplots()
    ax.plot(pu, dpt, 'r--')
    ax.plot(pu_msr, dpt_msr, 'ro')
    ax.plot(so, dpt, 'b--')
    ax.plot(so_msr, dpt_msr, 'bo')
    ax.plot(ro, dpt, 'k--')
    ax.plot(ro_msr, dpt_msr, 'ko')
    plt.gca().invert_yaxis()

    fig2, ax = plt.subplots()
    ax.plot(tq, dpt, 'r--')
    ax.plot(tq_msr, dpt_msr, 'ro')
    plt.gca().invert_yaxis()

    plt.show()

tnd_plot(task)
