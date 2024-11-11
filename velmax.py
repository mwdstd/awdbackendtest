import numpy as np
import matplotlib.pyplot as plt
import models.api as api
from dataset.surge_max_vel import task, v_ref


def velmax_plot(task):
    response = api.post('pooh_max_vel', task)
    v_vs_md = np.array([[pt['md'], pt['velocity']] for pt in response['graph']])
    plt.figure()
    plt.plot(v_vs_md[:, 0], v_vs_md[:, 1], 'ro-', label='Vmax')
    plt.plot(v_ref[:, 0], v_ref[:, 1], 'g-', label='Vref')
    plt.xlabel('MD, m')
    plt.ylabel('Max drill pipe velocity, m/s')
    plt.legend()
    plt.ylim(bottom=0.)
    plt.show()


if __name__ == '__main__':
    velmax_plot(task)