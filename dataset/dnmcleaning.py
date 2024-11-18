import copy
import numpy as np
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
              "innerDiameter": 0.07,
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

mcut_vs_t_inc80_rpm90 = np.array([[0, 7],
                                [123, 52],
                                [246, 98],
                                [373, 143],
                                [496, 189],
                                [635, 234],
                                [758, 280],
                                [833, 293],
                                [952, 290],
                                [1086, 288],
                                [1193, 291],
                                [1284, 297],
                                [1374, 292],
                                [1390, 311],
                                [1437, 280],
                                [1480, 234],
                                [1563, 189],
                                [1669, 171],
                                [1780, 163],
                                [1906, 172],
                                [2009, 167],
                                [2068, 166],
                                [2139, 186],
                                [2212, 161],
                                [2327, 111],
                                [2430, 73],
                                [2552, 34],
                                [2651, 12],
                                [2738, 6],
                                [2868, 2],
                                [2990, 1],
                                [3133, 0]])

mcut_vs_t_inc80_rpm50 = np.array([[0, 1],
                                [148, 45],
                                [274, 90],
                                [413, 137],
                                [534, 181],
                                [660, 227],
                                [777, 266],
                                [1017, 270],
                                [1159, 264],
                                [1297, 260],
                                [1404, 262],
                                [1515, 270],
                                [1591, 269],
                                [1618, 277],
                                [1693, 257],
                                [1737, 263],
                                [1817, 245],
                                [1883, 234],
                                [1954, 224],
                                [1999, 232],
                                [2061, 228],
                                [2173, 250],
                                [2235, 242],
                                [2302, 250],
                                [2351, 243],
                                [2413, 259],
                                [2501, 227],
                                [2620, 181],
                                [2735, 136],
                                [2862, 92],
                                [2986, 65],
                                [3114, 46],
                                [3190, 37],
                                [3279, 36],
                                [3500, 30]])

mcut_vs_t_inc65_300gpm = np.array([[0, 0],
                                    [265, 90],
                                    [510, 180],
                                    [746, 271],
                                    [986, 361],
                                    [1206, 433],
                                    [1490, 444],
                                    [1815, 444],
                                    [1830, 455],
                                    [1994, 391],
                                    [2193, 337],
                                    [2372, 296],
                                    [2486, 283],
                                    [2731, 284],
                                    [2870, 271],
                                    [2995, 240],
                                    [3219, 226],
                                    [3413, 220],
                                    [3543, 215],
                                    [3767, 183]])