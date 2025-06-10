from dataset.traj import task_tvd2md
import models.api as api


if __name__ == '__main__':
    endpoint = 'tvd2md'
    task_tvd2md['tvd'] = -100.
    print(api.post(endpoint, task_tvd2md)['md'])
    task_tvd2md['tvd'] = 1000.
    print(api.post(endpoint, task_tvd2md)['md'])
    task_tvd2md['tvd'] = 2500.
    print(api.post(endpoint, task_tvd2md)['md'])
    task_tvd2md['tvd'] = 5000.
    print(api.post(endpoint, task_tvd2md)['md'])