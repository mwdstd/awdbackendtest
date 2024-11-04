import requests
import json
import numpy as np
from models.tkn import get_token
from dataset.hydr_hor_well import task, spp, ecd, esd
import matplotlib.pyplot as plt


url = 'http://localhost:8000/calc/hydr_broomstick'

tkn = "Bearer " + get_token()
headers = {
    'accept': 'application/json',
    'Authorization': tkn,
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(task)).json()
spp_model = np.array([[pt['md'], pt['pressurePipe'] / 1e5] for pt in response['graph']])
spp_measure = np.array([[pt['md'], pt['spp']] for pt in spp])
fig1, ax = plt.subplots()
ax.plot(spp_model[:, 0], spp_model[:, 1], 'r-')
ax.plot(spp_measure[:, 0], spp_measure[:, 1], 'go-')
# plt.gca().invert_yaxis()


ecd_model = np.array([[pt['md'], pt['ecd']] for pt in response['graph']])
esd = np.array([[pt['md'], pt['esd'] * 1000] for pt in esd])
esd_int = np.interp(ecd_model[:, 0], esd[:, 0], esd[:, 1])
ecd_model[:, 1] = ecd_model[:, 1] - task["mud"]["mw"] + esd_int
ecd_measure = np.array([[pt['md'], pt['ecd'] * 1000] for pt in ecd])
fig2, ax = plt.subplots()
ax.plot(ecd_model[:, 0], ecd_model[:, 1], 'r-')
ax.plot(ecd_measure[:, 0], ecd_measure[:, 1], 'go-')
# plt.gca().invert_yaxis()

plt.show()
a = 1