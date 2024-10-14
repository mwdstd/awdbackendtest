units = {
        "metric": "m",
        "volume": "m^3",
        "density": "kg/m^3",
        "weight": "t",
        "torque": "N*m",
        "money": "$"
    }

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

iscwsa3 = {
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
            {'az': 193.0, 'inc': 110.0, 'md': 4030.0}
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