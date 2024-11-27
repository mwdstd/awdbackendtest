import models.api as api
from dataset.rop_model import task


def rop(task):
    response = api.post('rop_model', task)
    print(response)


if __name__ == '__main__':
    rop(task)
