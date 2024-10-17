from dataset.units import units

iscwsa1 = {
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
            {"depth": None, "toolcode": "MWD0"}
        ],
        "reference": {"lat": 0, "lon": 0, "alt": 0, "g": 9.80665, "b": 50000, "dip": 72, "dec": -4, "grid": 0},
        "slotUncertainty": {"ns": 0, "ew": 0, "tvd": 0}
    },
    "mdStep": 30
}

ref_iscwsa1 = {'sh': 20.116, 'sl': 84.342, 'sa': 8.626, 'rhl': -0.016, 'rha': 0.676, 'rla': -0.004, 'ds': .05, 'dr': .01}

iscwsa3_leg1 = {
    "units": units,
    "well": {
        "name": "string",
        "head": {"ns": 0, "ew": 0, "tvd": 0},
        "stations": [
            {'az': 0.0, 'inc': 0.0, 'md': 0.0},
            {'az': 0.0, 'inc': 0.0, 'md': 500.0},
            {'az': 0.0, 'inc': 50.0, 'md': 1100.0},
            {'az': 0.0, 'inc': 50.0, 'md': 1380.0}
        ],
        "surveyProgram": [
            {"depth": 1380.0, "toolcode": "MWD0"}
        ],
        "reference": {"lat": 0, "lon": 0, "alt": 0, "g": 9.80665, "b": 61000, "dip": -70, "dec": 13, "grid": 0},
        "slotUncertainty": {"ns": 0, "ew": 0, "tvd": 0}
    },
    "mdStep": 30
}

ref_iscwsa3_leg1 = {'sh': 2.013, 'sl': 4.703, 'sa': 0.919, 'rhl': -0.007, 'rha': 0.633, 'rla': -0.006, 'ds': .05, 'dr': .01}

iscwsa3_leg2 = {
    "units": units,
    "well": {
        "name": "string",
        "head": {"ns": 0, "ew": 0, "tvd": 0},
        "stations": [
            {'az': 0.0, 'inc': 0.0, 'md': 0.0},
            {'az': 0.0, 'inc': 0.0, 'md': 500.0},
            {'az': 0.0, 'inc': 50.0, 'md': 1100.0},
            {'az': 0.0, 'inc': 50.0, 'md': 1380.0},
            {'az': 0.0, 'inc': 50.0, 'md': 1700.0},
            {'az': 0.0, 'inc': 0.0, 'md': 2450.0},
            {'az': 0.0, 'inc': 0.0, 'md': 2850.0},
            {'az': 283.0, 'inc': 75.0, 'md': 3000.0}
        ],
        "surveyProgram": [
            {"depth": 1380.0, "toolcode": "MWD0"},
            {"depth": 3000.0, "toolcode": "MWD0+AX"}
        ],
        "reference": {"lat": 0, "lon": 0, "alt": 0, "g": 9.80665, "b": 61000, "dip": -70, "dec": 13, "grid": 0},
        "slotUncertainty": {"ns": 0, "ew": 0, "tvd": 0}
    },
    "mdStep": 30
}

ref_iscwsa3_leg2 = {'sh': 3.239, 'sl': 3.646, 'sa': 7.890, 'rhl': -0.172, 'rha': 0.623, 'rla': -0.665, 'ds': .1, 'dr': .015}

iscwsa3_leg3 = {
    "units": units,
    "well": {
        "name": "string",
        "head": {"ns": 0, "ew": 0, "tvd": 0},
        "stations": [
            {'az': 0.0, 'inc': 0.0, 'md': 0.0},
            {'az': 0.0, 'inc': 0.0, 'md': 500.0},
            {'az': 0.0, 'inc': 50.0, 'md': 1100.0},
            {'az': 0.0, 'inc': 50.0, 'md': 1700.0},
            {'az': 0.0, 'inc': 0.0, 'md': 2450.0},
            {'az': 0.0, 'inc': 0.0, 'md': 2850.0},
            {'az': 283.0, 'inc': 90.0, 'md': 3030.0},
            {'az': 283.0, 'inc': 90.0, 'md': 3430.0},
            {'az': 193.0, 'inc': 110.0, 'md': 3730.0},
            {'az': 193.0, 'inc': 110.0, 'md': 4020.0}
        ],
        "surveyProgram": [
            {"depth": 1380.0, "toolcode": "MWD0"},
            {"depth": 3000.0, "toolcode": "MWD0+AX"},
            {"depth": None, "toolcode": "MWD0"}
        ],
        "reference": {"lat": 0, "lon": 0, "alt": 0, "g": 9.80665, "b": 61000, "dip": -70, "dec": 13, "grid": 0},
        "slotUncertainty": {"ns": 0, "ew": 0, "tvd": 0}
    },
    "mdStep": 30
}

ref_iscwsa3_leg3 = {'sh': 5.570, 'sl': 5.900, 'sa': 9.550, 'rhl': -0.184, 'rha': -0.590, 'rla': 0.305, 'ds': .1, 'dr': .01}
