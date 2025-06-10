from dataset.units import units


task_tvd2md = {
    "units": units,
    # trajectory tie-in point
    "head": {"ns": 0, "ew": 0, "tvd": 0},
    # trajectory
    "stations": [
        {'az': 0.0, 'inc': 0.0, 'md': 0.0},
        {'az': 0.0, 'inc': 0.0, 'md': 1200.0},
        {'az': 75.0, 'inc': 60.0, 'md': 2100.0},
        {'az': 75.0, 'inc': 60.0, 'md': 5100.0},
        {'az': 75.0, 'inc': 90.0, 'md': 5400.0},
        {'az': 75.0, 'inc': 90.0, 'md': 8000.0}
    ],
    # target TVD
    "tvd": 150.0
}