import copy
from dataset.units import units

task = {
  "units": units,
  "borehole": {
    "trajectory": [
        {"md":0, "inc":80, "az":0},
        {"md":30.5, "inc":80, "az":0}
    ],
    "borehole": [
        {
            "md": 30.5,
            "innerDiameter": 0.2032,
            "frictionFactors": {
                "slackOff": 0.2,
                "pickUp": 0.2,
                "torque": 0.2,
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
      {
          "length": 30.5,
          "element": {
              "youngModulus": 2.1e11,
              "shearModulus": 7.9e10,
              "materialDensity": 7860,
              "outerDiameter": 0.1143,
              "innerDiameter": 0.1143,
              "length": 30.5,
              "jointOuterDiameter": 0.1143,
              "jointHydraulicDiameter": 0.1143,
              "jointInnerDiameter": 0.07,
              "jointLength": 0.01,
              "criticalTorque": 3.85e4,
              "yieldPoint": 9.3e8,
              "linearWeight": 32.1,
              "pressureDrop": 0
        }

       }
    ],
    "openEnd": True,
    "bitHsi": 0
  },
  "mudsystem": [{"innerDiameter": 0.0635, "length": 0.1}],
  "mdStep": 30.5,
  "mud": {"mw": 1027, "ty": 0.4253, "k": 0.1566, "m": 0.6008},
  "cuttings": {"density": 2640, "concentration": 0.0, "diameter": 0.00635, "porosity": 0.45},
  "cuttingBed": [(30.5, 0)],
  "cuttingFlow": [(30.5, 0)],
  "flowRate": 0.022716,
  "rop": 0.004088,
  "rpm": 0,
  "timeStep": 4,
  "circulationTime": 1620,
  "timeData": True
}

# lab test 1
task_1_0 = copy.deepcopy(task)
task_1_1 = copy.deepcopy(task_1_0)
task_1_1["circulationTime"] = 740
task_1_1["rpm"] = 50
task_1_2 = copy.deepcopy(task_1_1)
task_1_2["circulationTime"] = 1140
task_1_2["rop"] = 0

# lab test 2
task_2_0 = copy.deepcopy(task)
task_2_0["circulationTime"] = 1400
task_2_1 = copy.deepcopy(task_2_0)
task_2_1["circulationTime"] = 840
task_2_1["rpm"] = 90
task_2_2 = copy.deepcopy(task_2_1)
task_2_2["circulationTime"] = 1200
task_2_2["rop"] = 0

# lab test 3
task_3_0 = copy.deepcopy(task)
task_3_0["circulationTime"] = 1800
task_3_0["cuttings"]["porosity"] = 0.39
task_3_1 = copy.deepcopy(task_3_0)
task_3_1["circulationTime"] = 900
task_3_1["rop"] = 0
task_3_2 = copy.deepcopy(task_3_1)
task_3_2["circulationTime"] = 500
task_3_2["rpm"] = 50
task_3_3 = copy.deepcopy(task_3_2)
task_3_3["circulationTime"] = 600
task_3_3["rpm"] = 75
