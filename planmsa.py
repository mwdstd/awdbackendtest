import models.api as api
from dataset.units import units

endpoint = 'planmsa'

task = {
    "units": units,
    "well": {
        "name": "string",
        "head": {"ns": 0, "ew": 0, "tvd": 0},
        "stations": [
            {'az': 0.0, 'inc': 0.0, 'md': 0.0},
            {'az': 0.0, 'inc': 0.0, 'md': 1200.0},
            {'az': 75.0, 'inc': 60.0, 'md': 2100.0},
            {'az': 75.0, 'inc': 60.0, 'md': 5100.0},
            {'az': 75.0, 'inc': 90.0, 'md': 5400.0},
            {'az': 75.0, 'inc': 90.0, 'md': 8000.0}
        ],
        "surveyProgram": [
            {"depth": 1000, "toolcode": "MWD"},
            {"depth": 5350, "toolcode": "MWD"},
            {"depth": None, "toolcode": "MWD"}
        ],
        "reference": {"lat": 0, "lon": 0, "alt": 0, "g": 9.80665, "b": 50000, "dip": 72, "dec": -4, "grid": 0},
        "slotUncertainty": {"ns": 0, "ew": 0, "tvd": 0}
    },
    "mdStep": 30
}



if __name__ == '__main__':
    response = api.post(endpoint, task)
    for k in response['result']:
        lst = response['result'][k]
        print(k)
        for i in lst:
            print(i)