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
  "rpm": 50,
  "timeStep": 4,
  "circulationTime": 1000,
  "timeData": True
}


hcl_ref = [{"md":145.8, "v_min":0.63, "c_bed":0.11},
            {"md":291.7, "v_min":0.64, "c_bed":0.12},
            {"md":437.5, "v_min":0.70, "c_bed":0.15},
            {"md":583.3, "v_min":0.85, "c_bed":0.20},
            {"md":729.2, "v_min":0.98, "c_bed":0.23},
            {"md":875.0, "v_min":1.14, "c_bed":0.26},
            {"md":1020.8, "v_min":1.23, "c_bed":0.27},
            {"md":1166.7, "v_min":1.21, "c_bed":0.27},
            {"md":1312.5, "v_min":1.16, "c_bed":0.26},
            {"md":1458.3, "v_min":1.08, "c_bed":0.25},
            {"md":1604.2, "v_min":1.02, "c_bed":0.22},
            {"md":1750.0, "v_min":0.97, "c_bed":0.21},
            {"md":1895.8, "v_min":1.01, "c_bed":0.22},
            {"md":2041.7, "v_min":1.16, "c_bed":0.24},
            {"md":2187.5, "v_min":1.33, "c_bed":0.28},
            {"md":2333.3, "v_min":1.42, "c_bed":0.29},
            {"md":2479.2, "v_min":1.43, "c_bed":0.30},
            {"md":2625.0, "v_min":1.43, "c_bed":0.30},
            {"md":2770.8, "v_min":1.42, "c_bed":0.29},
            {"md":2916.7, "v_min":1.40, "c_bed":0.29},
            {"md":3062.5, "v_min":1.44, "c_bed":0.30},
            {"md":3208.3, "v_min":1.49, "c_bed":0.31},
            {"md":3354.2, "v_min":1.49, "c_bed":0.31},
            {"md":3500.0, "v_min":1.67, "c_bed":0.26}]
