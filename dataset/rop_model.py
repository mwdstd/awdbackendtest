from numpy import pi
from dataset.units import units

task = {
    "units": units,
    "bit": {
        "diameter": 0.220,  # m, bit diameter
        "cutterCount": 50,  # number of cutters
        "cutterDiameter": 13e-3,  # m, cutter diameter
        "sideRakeAngle": 30,  # deg, alpha angle
        "backRakeAngle": 30,  # deg, teta angle
        "cutterWear": 2e-4,  # m, height of cutters' wear
        "cutterWearFactor": 2e-19,  # m3 / N / m
        "frictionFactor": 0.2,  # unitless, friction factor between the cutter and formation
        "ropCorrectionCoefficient": 1  # ROP model calibration coefficient, specific for bit model
    },
    "formation": {
        "abrasiveness": 10,  # unitless, [1..30]
        "brinellHardness": 290e6,  # Pa, HBW
        "uniaxialCompressiveStrength": 70e6  # Pa, UCS

    },
    "motor": {
        "diffPressureOffset": 2.4e6,  # Pa
        "revolutionsPerFlowVolume": 90,  # rev/m3
        "torqueToPressure": 750  # Pa/N/m
    },
    "surfaceRpm": 60,
    "weightOnBit": 150000,  # N
    "flowRate": 0.02,  # m3/s
    "drilledDistance": 100  # m
}
