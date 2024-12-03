import numpy as np
import matplotlib.pyplot as plt
import models.api as api
from dataset.hydr_hor_well import task, spp, ecd, esd


def broomstick_plot(task, spp, ecd, esd):
    response = api.post('hydr_broomstick', task)

    spp_model = np.array([[pt['md'], pt['pressurePipe'] / 1e5] for pt in response['graph']])
    spp_measure = np.array([[pt['md'], pt['spp']] for pt in spp])
    fig1, ax = plt.subplots()
    ax.plot(spp_model[:, 0], spp_model[:, 1], 'r-', label='SPP Calculated')
    ax.plot(spp_measure[:, 0], spp_measure[:, 1], 'go-', label='SPP Measured')
    ax.set_ylabel('SPP, atm')
    ax.set_xlabel('MD, m')
    plt.title('Stand Pipe Pressure vs Depth')
    ax.legend()

    ecd_model = np.array([[pt['md'], pt['ecd']] for pt in response['graph']])
    esd = np.array([[pt['md'], pt['esd'] * 1000] for pt in esd])
    esd_int = np.interp(ecd_model[:, 0], esd[:, 0], esd[:, 1])
    ecd_model[:, 1] = ecd_model[:, 1] - task["mud"]["mw"] + esd_int
    ecd_measure = np.array([[pt['md'], pt['ecd'] * 1000] for pt in ecd])
    fig2, ax = plt.subplots()
    ax.plot(ecd_model[:, 0], ecd_model[:, 1], 'r-', label='ECD Calculated')
    ax.plot(ecd_measure[:, 0], ecd_measure[:, 1], 'go-', label='ECD Measured')
    ax.set_ylabel('ECD, kg/m3')
    ax.set_xlabel('MD, m')
    plt.title('ECD vs Depth')
    ax.legend()


if __name__ == '__main__':
    broomstick_plot(task, spp, ecd, esd)
    plt.show()