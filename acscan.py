import numpy as np
import matplotlib.pyplot as plt
import models.api as api
from dataset.ac_iscwsa_r4 import task, ac_benchmark
from models.ac import plot_osf


def acscan_plot(task, case_id):
    response = api.post('acscan', task)
    osf_calc = np.array([[pt['depth1'], pt['osf']] for pt in response['scan']])
    osf_bnch = np.array([[pt['md'], pt['osf']] for pt in ac_benchmark])
    plot_osf(osf_calc, osf_bnch, case_id)


if __name__ == '__main__':
    acscan_plot(task, 'ISCWSA offset well #3')
    plt.show()