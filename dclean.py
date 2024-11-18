import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
import models.api as api
from dataset.dnmcleaning import task, mcut_vs_t_inc80_rpm90, mcut_vs_t_inc65_300gpm, mcut_vs_t_inc80_rpm50

def plot_m_cut_vs_t(m_cut, ts, mcut_vs_t_exp, title):
    plt.figure()
    plt.plot(ts, m_cut, 'r-', label='Model')
    plt.plot(mcut_vs_t_exp[:, 0], mcut_vs_t_exp[:, 1], 'go-', label='Experiment')
    plt.xlabel('Time, s')
    plt.ylabel('Cutting Weight in Annulus, kg')
    plt.title(title)
    plt.legend()
    plt.ylim(0, 500)

def hole_cleaning_plot(task):
    a_ann = np.pi * (task['borehole']['borehole'][0]['innerDiameter'] ** 2 - task['drillstring']['tubular'][0]['element']['outerDiameter'] ** 2) / 4
    v_ann = a_ann * 100 * .305

    # lab test 1
    task_1_0 = deepcopy(task)
    response = api.post('holeclean_dynm', task_1_0)
    task_1_1 = deepcopy(task_1_0)
    task_1_1['circulationTime'] = 740
    task_1_1['rpm'] = 50
    task_1_1['cuttingBed'] = [(elt['md'], elt['cuttingBed']) for elt in response['depthData']]
    task_1_1['cuttingFlow'] = [(elt['md'], elt['cuttingFlow']) for elt in response['depthData']]
    ct1 = np.array([[elt['time'], elt['bedSegments'][0]] for elt in response['timeData']])
    response = api.post('holeclean_dynm', task_1_1)
    task_1_2 = deepcopy(task_1_1)
    task_1_2['circulationTime'] = 1140
    task_1_2['rop'] = 0
    task_1_2['cuttingBed'] = [(elt['md'], elt['cuttingBed']) for elt in response['depthData']]
    task_1_2['cuttingFlow'] = [(elt['md'], elt['cuttingFlow']) for elt in response['depthData']]
    ct2 = np.array([[elt['time'] + ct1[-1, 0], elt['bedSegments'][0]] for elt in response['timeData']])
    response = api.post('holeclean_dynm', task_1_2)
    ct3 = np.array([[elt['time'] + ct2[-1, 0], elt['bedSegments'][0]] for elt in response['timeData']])
    ts = np.append(np.append(ct1[:, 0], ct2[:, 0]), ct3[:, 0])
    ct = np.append(np.append(ct1[:, 1], ct2[:, 1]), ct3[:, 1])
    m_cut = v_ann * task['cuttings']['density'] * ct

    plot_m_cut_vs_t(m_cut, ts, mcut_vs_t_inc80_rpm50, 'Sanchez data: 80 deg, 350 gpm, 50 rpm')

    # lab test 2
    task_2_0 = deepcopy(task)
    task_2_0['flowRate'] = 0.022085
    task_2_0['circulationTime'] = 1400
    response = api.post('holeclean_dynm', task_2_0)
    task_2_1 = deepcopy(task_2_0)
    task_2_1['circulationTime'] = 840
    task_2_1['rpm'] = 90
    task_2_1['cuttingBed'] = [(elt['md'], elt['cuttingBed']) for elt in response['depthData']]
    task_2_1['cuttingFlow'] = [(elt['md'], elt['cuttingFlow']) for elt in response['depthData']]
    ct1 = np.array([[elt['time'], elt['bedSegments'][0]] for elt in response['timeData']])
    response = api.post('holeclean_dynm', task_2_1)
    task_2_2 = deepcopy(task_2_1)
    task_2_2['circulationTime'] = 1200
    task_2_2['rop'] = 0
    task_2_2['cuttingBed'] = [(elt['md'], elt['cuttingBed']) for elt in response['depthData']]
    task_2_2['cuttingFlow'] = [(elt['md'], elt['cuttingFlow']) for elt in response['depthData']]
    ct2 = np.array([[elt['time'] + ct1[-1, 0], elt['bedSegments'][0]] for elt in response['timeData']])
    response = api.post('holeclean_dynm', task_2_2)
    ct3 = np.array([[elt['time'] + ct2[-1, 0], elt['bedSegments'][0]] for elt in response['timeData']])
    ts = np.append(np.append(ct1[:, 0], ct2[:, 0]), ct3[:, 0])
    ct = np.append(np.append(ct1[:, 1], ct2[:, 1]), ct3[:, 1])
    m_cut = v_ann * task['cuttings']['density'] * ct

    plot_m_cut_vs_t(m_cut, ts, mcut_vs_t_inc80_rpm90, 'Sanchez data: 80 deg, 350 gpm, 90 rpm')

    # lab test 3
    task_3_0 = deepcopy(task)
    task_3_0['borehole']['trajectory'] = [{"md":0, "inc":65, "az":0}, {"md":30.5, "inc":65, "az":0}]
    task_3_0['flowRate'] = 0.01893
    task_3_0["circulationTime"] = 1800
    task_3_0["cuttings"]["porosity"] = 0.39
    response = api.post('holeclean_dynm', task_3_0)
    task_3_1 = deepcopy(task_3_0)
    task_3_1['circulationTime'] = 900
    task_3_1['rop'] = 0
    task_3_1['cuttingBed'] = [(elt['md'], elt['cuttingBed']) for elt in response['depthData']]
    task_3_1['cuttingFlow'] = [(elt['md'], elt['cuttingFlow']) for elt in response['depthData']]
    ct1 = np.array([[elt['time'], elt['bedSegments'][0]] for elt in response['timeData']])
    response = api.post('holeclean_dynm', task_3_1)
    task_3_2 = deepcopy(task_3_1)
    task_3_2['circulationTime'] = 500
    task_3_2['rpm'] = 50
    task_3_2['cuttingBed'] = [(elt['md'], elt['cuttingBed']) for elt in response['depthData']]
    task_3_2['cuttingFlow'] = [(elt['md'], elt['cuttingFlow']) for elt in response['depthData']]
    ct2 = np.array([[elt['time'] + ct1[-1, 0], elt['bedSegments'][0]] for elt in response['timeData']])
    response = api.post('holeclean_dynm', task_3_2)
    task_3_3 = deepcopy(task_3_2)
    task_3_3['circulationTime'] = 600
    task_3_3['rpm'] = 75
    task_3_3['cuttingBed'] = [(elt['md'], elt['cuttingBed']) for elt in response['depthData']]
    task_3_3['cuttingFlow'] = [(elt['md'], elt['cuttingFlow']) for elt in response['depthData']]
    ct3 = np.array([[elt['time'] + ct2[-1, 0], elt['bedSegments'][0]] for elt in response['timeData']])
    response = api.post('holeclean_dynm', task_3_3)
    ct4 = np.array([[elt['time'] + ct3[-1, 0], elt['bedSegments'][0]] for elt in response['timeData']])
    ts = np.append(np.append(np.append(ct1[:, 0], ct2[:, 0]), ct3[:, 0]), ct4[:, 0])
    ct = np.append(np.append(np.append(ct1[:, 1], ct2[:, 1]), ct3[:, 1]), ct4[:, 1])
    m_cut = v_ann * task['cuttings']['density'] * ct

    plot_m_cut_vs_t(m_cut, ts, mcut_vs_t_inc65_300gpm, 'Sanchez data: 65 deg, 300 gpm, 50 and 75 rpm')



if __name__ == '__main__':
    hole_cleaning_plot(task)
    plt.show()