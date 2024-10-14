import requests
import json
import numpy as np
from tkn import get_token
from dataset.iscwsa import iscwsa1, ref_iscwsa1
from dataset.iscwsa import iscwsa3_leg1, ref_iscwsa3_leg1, iscwsa3_leg2, ref_iscwsa3_leg2, iscwsa3_leg3, ref_iscwsa3_leg3
from dataset.iscwsa_r4 import iscwsa_r4, ref_iscwsa_r4, hla_iscwsa_r4
from models.ac import cnev2axis, assert_eou, plot_hla

url = 'http://localhost:8000/calc/wellunc'

tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}

def eou_test(task, qc, case_id):
    response = requests.post(url, headers=headers, data=json.dumps(task)).json()
    traj = np.array([[s['md'], np.deg2rad(s['inc']), np.deg2rad(s['az'])] for s in response['stations']])
    covmat = np.array([[[s['snn'], s['sne'], s['snv']],
                      [s['sne'], s['see'], s['sev']],
                      [s['snv'], s['sev'], s['svv']]] for s in response['stations']])
    assert_eou(covmat[-1], traj[-1, 1], traj[-1, 2], qc, case_id)

def eou_plot(task, hla_ref_dict):
    response = requests.post(url, headers=headers, data=json.dumps(task)).json()
    traj = np.array([[s['md'], np.deg2rad(s['inc']), np.deg2rad(s['az'])] for s in response['stations']])
    covmat = np.array([[[s['snn'], s['sne'], s['snv']],
                      [s['sne'], s['see'], s['sev']],
                      [s['snv'], s['sev'], s['svv']]] for s in response['stations']])
    plot_hla(covmat, traj[:, 0], traj[:, 1], traj[:, 2], hla_ref_dict)


# eou_test(iscwsa1, ref_iscwsa1, 'iscwsa1')
# eou_test(iscwsa3_leg1, ref_iscwsa3_leg1, 'iscwsa3 leg1')
# eou_test(iscwsa3_leg2, ref_iscwsa3_leg2, 'iscwsa3 leg2')
# eou_test(iscwsa3_leg3, ref_iscwsa3_leg3, 'iscwsa3 leg3')
eou_plot(iscwsa_r4, hla_iscwsa_r4)
