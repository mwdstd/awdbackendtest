import numpy as np
import matplotlib.pyplot as plt
import models.api as api
from dataset.holecleaning import task, hcl_ref


def hole_cleaning_plot(task):
    response = api.post('holeclean_stat', task)

    v_ref = np.array([[pt['md'], pt['v_min']] for pt in hcl_ref])
    c_ref = np.array([[pt['md'], pt['c_bed']] for pt in hcl_ref])
    v_cal = np.array([[pt['md'], pt['velocity']] for pt in response['graph']])
    c_cal = np.array([[pt['md'], pt['cuttings']] for pt in response['graph']])

    fig1, ax = plt.subplots()
    ax.plot(v_cal[:, 0], v_cal[:, 1], 'r-', label='Calculated')
    ax.plot(v_ref[:, 0], v_ref[:, 1], 'go-', label='Measured')
    ax.set_title('Minimal mud annular velocity')
    ax.set_xlabel('Measured Depth, m')
    ax.set_ylabel('Minimal velocity, m/s')
    ax.legend()

    fig2, ax = plt.subplots()
    ax.plot(c_cal[:, 0], c_cal[:, 1], 'r-', label='Calculated')
    ax.plot(c_ref[:, 0], c_ref[:, 1], 'go-', label='Measured')
    ax.set_title('Cutting Bed')
    ax.set_xlabel('Measured Depth, m')
    ax.set_ylabel('Cutting Bed')
    ax.legend()


if __name__ == '__main__':
    hole_cleaning_plot(task)
    plt.show()