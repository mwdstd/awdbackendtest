import numpy as np
from numpy import sin, cos, sqrt
import matplotlib.pyplot as plt


def cnev2axis(cnev, inc, az):
    r = np.array([[cos(inc) * cos(az), -sin(az), sin(inc) * cos(az)],
                  [cos(inc) * sin(az), cos(az), sin(inc) * sin(az)],
                  [-sin(inc), 0, cos(inc)]])
    chla = r.T @ cnev @ r
    sh = sqrt(chla[0, 0])
    sl = sqrt(chla[1, 1])
    sa = sqrt(chla[2, 2])
    rhl = chla[0, 1] / sh / sl
    rha = chla[0, 2] / sh / sa
    rla = chla[1, 2] / sl / sa
    return sh, sl, sa, rhl, rha, rla


def assert_eou(cnev, inc, az, ref, case_id):
    sh, sl, sa, rhl, rha, rla = cnev2axis(cnev, inc, az)
    sh0, sl0, sa0 = ref['sh'], ref['sl'], ref['sa']
    rhl0, rha0, rla0 = ref['rhl'], ref['rha'], ref['rla']
    ds, dr = ref['ds'], ref['dr']
    print(f'Ref EOU: sh={sh0:.2f}m, sl={sl0:.2f}m, sa={sa0:.2f}m, rhl={rhl0:.2f}, rha={rha0:.2f}, rla={rla0:.2f}')
    print(f'Act EOU: sh={sh:.2f}m, sl={sl:.2f}m, sa={sa:.2f}m, rhl={rhl:.2f}, rha={rha:.2f}, rla={rla:.2f}')
    assert (max(abs(sh - sh0), abs(sl - sl0), abs(sa - sa0)) < ds and
            max(abs(rhl - rhl0), abs(rha - rha0), abs(rla - rla0)) < dr), f'EOU test of {case_id} failed'

def plot_hla(cnev, md, inc, az, hla_ref_dict):
    hla_calc = np.array([cnev2axis(c, i, a) for c, i, a in zip(cnev, inc, az)])
    hla_ref = np.array([[hla['sh'], hla['sl'], hla['sa']] for hla in hla_ref_dict])
    plt.figure()
    plt.plot(md, hla_calc[:, 0], 'r-', label='Sh calc')
    plt.plot(md, hla_calc[:, 1], 'g-', label='Sl calc')
    plt.plot(md, hla_calc[:, 2], 'b-', label='Sa calc')
    plt.plot(md, hla_ref[:, 0], 'r.', label='Sh ref')
    plt.plot(md, hla_ref[:, 1], 'g.', label='Sl ref')
    plt.plot(md, hla_ref[:, 2], 'b.', label='Sa ref')
    plt.xlabel('MD, m')
    plt.ylabel('Semi-axis, m')
    plt.legend()
    plt.show()