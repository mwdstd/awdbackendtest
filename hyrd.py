import requests
import json
import numpy as np
from models.tkn import get_token
from dataset.hydr_hor_well import task, spp
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
ax.plot(spp_model[:, 1], spp_model[:, 0], 'r-')
ax.plot(spp_measure[:, 1], spp_measure[:, 0], 'go')
plt.gca().invert_yaxis()

# fig2, ax = plt.subplots()
# ax.plot(tq, dpt, 'r--')
# ax.plot(tq_msr, dpt_msr, 'ro')
# plt.gca().invert_yaxis()

plt.show()
a = 1