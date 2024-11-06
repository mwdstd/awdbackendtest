from dataset.units import units

pipe1 = {
          "youngModulus": 2.1e11,
          "shearModulus": 7.9e10,
          "materialDensity": 7860,
          "outerDiameter": 0.127,
          "innerDiameter": 0.1086,
          "length": 9.6,
          "jointOuterDiameter": 0.17145,
          "jointHydraulicDiameter": 0.17145,
          "jointInnerDiameter": 0.07,
          "jointLength": 0.53,
          "criticalTorque": 3.85e4,
          "yieldPoint": 9.3e8,
          "linearWeight": 32.1,
          "pressureDrop": 0
        }
pipe2 = {
          "youngModulus": 2.1e11,
          "shearModulus": 7.9e10,
          "materialDensity": 7860,
          "outerDiameter": 0.127,
          "innerDiameter": 0.1086,
          "length": 9.6,
          "jointOuterDiameter": 0.1651,
          "jointHydraulicDiameter": 0.1651,
          "jointInnerDiameter": 0.0762,
          "jointLength": 0.53,
          "criticalTorque": 3.85e4,
          "yieldPoint": 9.3e8,
          "linearWeight": 32.1,
          "pressureDrop": 0
        }
hwdc1 = {
          "youngModulus": 2.1e11,
          "shearModulus": 7.9e10,
          "materialDensity": 7860,
          "outerDiameter": 0.127,
          "innerDiameter": 0.0572,
          "length": 5.71,
          "jointOuterDiameter": 0.127,
          "jointHydraulicDiameter": 0.127,
          "jointInnerDiameter": 0.0572,
          "jointLength": 0.01,
          "criticalTorque": 3.85e4,
          "yieldPoint": 9.3e8,
          "linearWeight": 82.5,
          "pressureDrop": 0
        }
hwdc2 = {
          "youngModulus": 2.1e11,
          "shearModulus": 7.9e10,
          "materialDensity": 7860,
          "outerDiameter": 0.1486,
          "innerDiameter": 0.0572,
          "length": 2.35,
          "jointOuterDiameter": 0.1486,
          "jointHydraulicDiameter": 0.1486,
          "jointInnerDiameter": 0.0572,
          "jointLength": 0.01,
          "criticalTorque": 3.85e4,
          "yieldPoint": 9.3e8,
          "linearWeight": 82.5,
          "pressureDrop": 0
        }

task = {
  "units": units,
  "borehole": {
    "trajectory": [
        {"md":0, "inc":0, "az":0},
        {"md":600, "inc":0, "az":0},
        {"md":1000, "inc":18, "az":0},
        {"md":1750, "inc":18, "az":0},
        {"md":2750, "inc":12, "az":0},
        {"md":3800, "inc":10, "az":0},
    ],
    "borehole": [
        {
            "md": 3800,
            "innerDiameter": 0.27206,
            "frictionFactors": {
                "slackOff": 0.22,
                "pickUp": 0.21,
                "torque": 0.22,
                "rotation": 0.01
            },
            "tortuosity": 0,
            "mudWindow": [1000, 3000]
        }
    ],
    "bopPressure": 0
  },
  "drillstring": {
    "tubular": [
      {"length": 1032.5, "element": pipe1},
      {"length": 5.7, "element": hwdc1},
      {"length": 2.4, "element": hwdc2},
      {"length": 1518.4, "element": pipe1},
      {"length": 5.7, "element": hwdc1},
      {"length": 2.4, "element": hwdc2},
      {"length": 459.1, "element": pipe1},
      {"length": 751.4, "element": pipe2},
      {"length": 5.7, "element": hwdc1},
      {"length": 5.7, "element": hwdc1},
      {"length": 2.4, "element": hwdc2},
    ],
    "openEnd": False,
    "bitHsi": 2.32
  },
  "mdStep": 200,
  "topDepth": 3790,
  "mud": {"mw": 1380, "ty": 3.2, "k": 0.28, "m": 0.8},
  "pipeVelocity": 0
}

# drillstring velocity (m/s) vs surge/swab pressure (bar)
dp_vp = [[-0.50, -7.38],
         [-0.46, -6.10],
         [-.305, -6.15],
         [-0.08, -4.41],
         [0.076, 3.266],
         [0.315, 5.725]]