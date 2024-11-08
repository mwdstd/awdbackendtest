import requests
import json
import matplotlib.pyplot as plt
from models.tkn import get_token
from dataset.tnd_hor_well import task, drillmech


tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}

def broomstick_plot(task):
    url = 'http://localhost:8000/calc/tnd_broomstick'
    response = requests.post(url, headers=headers, data=json.dumps(task)).json()
    block_weight = 37  # tons

    dpt = [pnt['md'] for pnt in response['graph']]
    so = [pnt['dragRih'] + block_weight for pnt in response['graph']]
    pu = [pnt['dragPoh'] + block_weight for pnt in response['graph']]
    ro = [pnt['dragRot'] + block_weight for pnt in response['graph']]
    tq = [pnt['torque'] / 1000 for pnt in response['graph']]

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

def snapshot_plot(task, scenario):
    url = 'http://localhost:8000/calc/tnd_snapshot'
    response = requests.post(url, headers=headers, data=json.dumps(task)).json()

    def plot_scenario(response):
        dpt = [pnt['md'] for pnt in response[scenario]]
        drag = [pnt['drag'] for pnt in response[scenario]]
        torq = [pnt['torque'] / 1000 for pnt in response[scenario] if 'torque' in pnt]
        sfrc = [pnt['sideforce'] / 9.81 / 1000 for pnt in response[scenario]]
        sbkl = [-pnt['bucklingSin'] if pnt['bucklingSin'] is not None else None for pnt in response[scenario]]
        hbkl = [-pnt['bucklingHel'] if pnt['bucklingHel'] is not None else None for pnt in response[scenario]]

        fig1, ax = plt.subplots()
        ax.plot(drag, dpt, 'b-')
        # ax.plot(sfrc, dpt, 'b--')
        ax.plot(sbkl, dpt, 'y-')
        ax.plot(hbkl, dpt, 'r-')
        ax.set_xlabel('Drag, t')
        ax.set_ylabel('MD, m')
        plt.gca().invert_yaxis()
        ax.grid(True)

        if len(torq) > 0:
            fig2, ax = plt.subplots()
            ax.plot(torq, dpt, 'b-')
            ax.set_xlabel('Torque, kN.m')
            ax.set_ylabel('MD, m')
            plt.gca().invert_yaxis()
            ax.grid(True)

        plt.title(f'{scenario}')
        # plt.legend()
        plt.show()

    plot_scenario(response)

# scenario: runIn, pullOut, slide, rotor, reamUp
snapshot_plot(task, 'slide')
broomstick_plot(task)