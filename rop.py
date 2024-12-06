import matplotlib.pyplot as plt
import models.api as api
from dataset.rop_model import task, rop_ref


def rop(task):
    modeled_rop = []
    measured_rop = [elt['rop'] for elt in rop_ref]
    md = [elt['md'] for elt in rop_ref]
    for _ in range(len(md)):
        response = api.post('rop_model', task)
        # print(response)
        task['bit']['cutterWear'] = response['updatedBitWear']
        modeled_rop += [response['rop']]
    fig, ax = plt.subplots()
    ax.plot(md, modeled_rop, 'r-', label='Modeled ROP')
    ax.plot(md, measured_rop, 'go-', label='Measured ROP')
    ax.set_ylabel('ROP, m/hrs')
    ax.set_ylim(0, 40)
    ax.set_xlabel('MD, m')
    plt.title('Modeled ROP with Bit Wear')
    ax.legend()


if __name__ == '__main__':
    rop(task)
    plt.show()
