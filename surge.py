import requests
import json
import numpy as np
from models.tkn import get_token
from dataset.surge_swab_well import task, dp_vp
import matplotlib.pyplot as plt


tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}


def broomstick_plot(task):
    url = 'http://localhost:8000/calc/surge_swab_broomstick'
    dp = []
    for vp, _ in dp_vp:
        task["pipeVelocity"] = vp
        response = requests.post(url, headers=headers, data=json.dumps(task)).json()
        dp += [response["graph"][0]["pressureDrop"] / 1e5]

    labels = [str(vp) for vp, _ in dp_vp]
    ticks = np.arange(len(dp))
    bar_width = 0.35

    fig, ax = plt.subplots()
    ax.bar(ticks, dp, width=bar_width, color='r', label='Calculated')
    ax.bar(ticks + bar_width, [dp for _, dp in dp_vp], width=bar_width, color='g', label='Measured')
    ax.set_xticks(ticks + bar_width / 2)
    ax.set_xticklabels(labels)
    ax.set_title('Annulus Δ Pressure due to Surge/Swab')
    ax.set_xlabel('Drillstring Velocity, m/s')
    ax.set_ylabel('ΔPressure, bar')
    ax.legend()
    plt.show()


def snapshot_plot(task):
    url = 'http://localhost:8000/calc/surge_swab_broomstick'
    dp = []
    for vp, _ in dp_vp:
        task["pipeVelocity"] = vp
        response = requests.post(url, headers=headers, data=json.dumps(task))
        response = response.json()
        dp += [response["graph"][0]["pressureDrop"] / 1e5]

    labels = [str(vp) for vp, _ in dp_vp]
    ticks = np.arange(len(dp))
    bar_width = 0.35

    fig, ax = plt.subplots()
    ax.bar(ticks, dp, width=bar_width, color='r', label='Calculated')
    ax.bar(ticks + bar_width, [dp for _, dp in dp_vp], width=bar_width, color='g', label='Measured')
    ax.set_xticks(ticks + bar_width / 2)
    ax.set_xticklabels(labels)
    ax.set_title('Annulus Δ Pressure due to Surge/Swab')
    ax.set_xlabel('Drillstring Velocity, m/s')
    ax.set_ylabel('ΔPressure, bar')
    ax.legend()
    plt.show()


broomstick_plot(task)
