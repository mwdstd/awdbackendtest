import numpy as np
import matplotlib.pyplot as plt
import models.api as api
from dataset.eou_iscwsa_r0 import iscwsa1, ref_iscwsa1
from dataset.eou_iscwsa_r0 import iscwsa3_leg1, ref_iscwsa3_leg1, iscwsa3_leg2, ref_iscwsa3_leg2, iscwsa3_leg3, ref_iscwsa3_leg3
from dataset.eou_iscwsa_r4 import iscwsa_r4, hla_iscwsa_r4
from models.ac import assert_eou, plot_hla


endpoint = 'wellunc'


def eou_test(task, qc, case_id):
    response = api.post(endpoint, task)
    traj = np.array([[s['md'], np.deg2rad(s['inc']), np.deg2rad(s['az'])] for s in response['stations']])
    covmat = np.array([[[s['snn'], s['sne'], s['snv']],
                      [s['sne'], s['see'], s['sev']],
                      [s['snv'], s['sev'], s['svv']]] for s in response['stations']])
    assert_eou(covmat[-1], traj[-1, 1], traj[-1, 2], qc, case_id)


def eou_plot(task, hla_ref_dict, case_id):
    response = api.post(endpoint, task)
    traj = np.array([[s['md'], np.deg2rad(s['inc']), np.deg2rad(s['az'])] for s in response['stations']])
    covmat = np.array([[[s['snn'], s['sne'], s['snv']],
                      [s['sne'], s['see'], s['sev']],
                      [s['snv'], s['sev'], s['svv']]] for s in response['stations']])
    plot_hla(covmat, traj[:, 0], traj[:, 1], traj[:, 2], hla_ref_dict, case_id)


if __name__ == '__main__':
    eou_test(iscwsa1, ref_iscwsa1, 'ISCWSA1')
    eou_test(iscwsa3_leg1, ref_iscwsa3_leg1, 'ISCWSA3 Leg1')
    eou_test(iscwsa3_leg2, ref_iscwsa3_leg2, 'ISCWSA3 Leg2')
    eou_test(iscwsa3_leg3, ref_iscwsa3_leg3, 'ISCWSA3 Leg3')
    eou_plot(iscwsa_r4, hla_iscwsa_r4, 'ISCWSA Rev4 EOU Test')
    plt.show()
