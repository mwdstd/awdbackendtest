import numpy as np
import matplotlib.pyplot as plt
import models.api as api
from dataset.surge_swab_well import task, dp_vp


def broomstick_plot(task):
    dp = []
    for vp, _ in dp_vp:
        task["pipeVelocity"] = vp
        response = api.post('surge_swab_broomstick', task)
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


def snapshot_plot(task):
    response = api.post('surge_swab_snapshot', task)
    dp_vs_md = np.array([[pt["md"], pt["pressureDrop"] / 1e5] for pt in response["graph"]])

    fig1, ax = plt.subplots()
    ax.plot(dp_vs_md[:, 1], dp_vs_md[:, 0], 'b-')
    ax.set_xlabel('Pressure Drop, atm')
    ax.set_ylabel('Measured Depth, m')
    plt.gca().invert_yaxis()
    ax.grid(True)


if __name__ == '__main__':
    snapshot_plot(task)
    broomstick_plot(task)
    plt.show()