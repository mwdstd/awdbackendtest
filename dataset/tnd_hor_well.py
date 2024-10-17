from dataset.units import units


pipe = {
          "youngModulus": 2.1e11,
          "shearModulus": 7.9e10,
          "materialDensity": 7860,
          "outerDiameter": 0.127,
          "innerDiameter": 0.1104,
          "length": 14.3,
          "jointOuterDiameter": 0.168,
          "jointHydraulicDiameter": 0.168,
          "jointInnerDiameter": 0.08,
          "jointLength": 0.8,
          "criticalTorque": 3.85e4,
          "yieldPoint": 9.3e8,
          "linearWeight": 32.1,
          "pressureDrop": 0
        }
hwdp = {
          "youngModulus": 2.1e11,
          "shearModulus": 7.9e10,
          "materialDensity": 7860,
          "outerDiameter": 0.127,
          "innerDiameter": 0.076,
          "length": 9.2,
          "jointOuterDiameter": 0.168,
          "jointHydraulicDiameter": 0.168,
          "jointInnerDiameter": 0.0762,
          "jointLength": 0.8,
          "criticalTorque": 4.27e4,
          "yieldPoint": 9.3e8,
          "linearWeight": 82.5,
          "pressureDrop": 0
        }
bha = {
          "youngModulus": 2.1e11,
          "shearModulus": 7.9e10,
          "materialDensity": 7860,
          "outerDiameter": 0.170,
          "innerDiameter": 0.076,
          "length": 55.0,
          "jointOuterDiameter": 0.170,
          "jointHydraulicDiameter": 0.170,
          "jointInnerDiameter": 0.0762,
          "jointLength": 0.01,
          "criticalTorque": 3.6e4,
          "yieldPoint": 9.3e8,
          "linearWeight": 148.0,
          "pressureDrop": 150.e5
        }

task = {
  "units": units,
  "borehole": {
    "trajectory": [
        {'md':0, 'inc':0, 'az':0},
        {'md':100, 'inc':1.46, 'az':343.69},
        {'md':200, 'inc':1.63, 'az':21.34},
        {'md':300, 'inc':1.3, 'az':102.39},
        {'md':400, 'inc':6.5, 'az':4.61},
        {'md':500, 'inc':14.97, 'az':1.91},
        {'md':600, 'inc':21.35, 'az':359.92},
        {'md':700, 'inc':23.75, 'az':356.98},
        {'md':800, 'inc':33.97, 'az':358.57},
        {'md':900, 'inc':39.76, 'az':0.76},
        {'md':1000, 'inc':39.53, 'az':359.05},
        {'md':1100, 'inc':40.97, 'az':358.32},
        {'md':1200, 'inc':36.67, 'az':3.57},
        {'md':1300, 'inc':31.87, 'az':11.43},
        {'md':1400, 'inc':28.61, 'az':12.91},
        {'md':1500, 'inc':25.35, 'az':19.72},
        {'md':1600, 'inc':22.5, 'az':40.27},
        {'md':1700, 'inc':21.92, 'az':68.29},
        {'md':1800, 'inc':20.28, 'az':94.83},
        {'md':1900, 'inc':29.19, 'az':106.91},
        {'md':2000, 'inc':37.51, 'az':121.93},
        {'md':2100, 'inc':48.08, 'az':127.5},
        {'md':2200, 'inc':55.33, 'az':130.5},
        {'md':2300, 'inc':54.38, 'az':130.5},
        {'md':2400, 'inc':54.01, 'az':130.5},
        {'md':2500, 'inc':55.61, 'az':130.5},
        {'md':2600, 'inc':55.4, 'az':130.5},
        {'md':2700, 'inc':53.56, 'az':130.5},
        {'md':2800, 'inc':52.61, 'az':130.5},
        {'md':2900, 'inc':53.6, 'az':130.5},
        {'md':3000, 'inc':54.93, 'az':130.5},
        {'md':3100, 'inc':61.42, 'az':130.5},
        {'md':3200, 'inc':70.85, 'az':130.5},
        {'md':3300, 'inc':83.51, 'az':130.5},
        {'md':3400, 'inc':87.48, 'az':130.5},
        {'md':3500, 'inc':90.58, 'az':130.5}
    ],
    "borehole": [
        {
            "md": 1515,
            "innerDiameter": 0.2285,
            "frictionFactors": {
                "slackOff": 0.19,
                "pickUp": 0.21,
                "torque": 0.22,
                "rotation": 0.01
            },
            "tortuosity": 0,
            "mudWindow": [None, None]
        },
        {
            "md": 3500,
            "innerDiameter": 0.2223,
            "frictionFactors": {
                "slackOff": 0.19,
                "pickUp": 0.22,
                "torque": 0.22,
                "rotation": 0.01
            },
            "tortuosity": 0,
            "mudWindow": [None, None]
        }
    ],
    "bopPressure": 0
  },
  "drillstring": {
    "drillstring": [
      {"length": 3075, "element": pipe},
      {"length": 85, "element": hwdp},
      {"length": 255, "element": pipe},
      {"length": 30, "element": hwdp},
      {"length": 55, "element": bha},
    ],
    "openEnd": True,
    "bitHsi": 0
  },
  "drillparams": {
    "weightOnBit": 0,
    "slackOffWeight": 0,
    "pickUpWeight": 0,
    "torqueOnBit": 0,
    "flowRate": 0,
    "pipeVelocity": 0,
    "rpm": 0
  },
  "mudWeight": 1150.,
  "mdStep": 100
}

drillmech = [{'md':1524, 'pu':92, 'rot':76, 'so':84, 'tq':8.0},
            {'md':1553, 'pu':93, 'rot':76, 'so':82, 'tq':8.0},
            {'md':1582, 'pu':95, 'rot':77, 'so':83, 'tq':8.0},
            {'md':1610, 'pu':94, 'rot':78, 'so':84, 'tq':8.0},
            {'md':1639, 'pu':96, 'rot':78, 'so':84, 'tq':9.0},
            {'md':1668, 'pu':97, 'rot':79, 'so':85, 'tq':9.0},
            {'md':1696, 'pu':98, 'rot':79, 'so':87, 'tq':10.0},
            {'md':1725, 'pu':99, 'rot':80, 'so':87, 'tq':10.0},
            {'md':1754, 'pu':101, 'rot':81, 'so':88, 'tq':12.0},
            {'md':1782, 'pu':101, 'rot':81, 'so':88, 'tq':14.0},
            {'md':1811, 'pu':104, 'rot':81, 'so':90, 'tq':13.0},
            {'md':1840, 'pu':103, 'rot':83, 'so':92, 'tq':13.0},
            {'md':1869, 'pu':103, 'rot':84, 'so':93, 'tq':14.0},
            {'md':1897, 'pu':103, 'rot':84, 'so':93, 'tq':15.0},
            {'md':1926, 'pu':109, 'rot':82, 'so':94, 'tq':14.0},
            {'md':1955, 'pu':110, 'rot':82, 'so':95, 'tq':15.0},
            {'md':1983, 'pu':112, 'rot':83, 'so':96, 'tq':16.0},
            {'md':2012, 'pu':113, 'rot':83, 'so':93, 'tq':16.0},
            {'md':2041, 'pu':114, 'rot':83, 'so':94, 'tq':16.0},
            {'md':2069, 'pu':115, 'rot':83, 'so':94, 'tq':16.0},
            {'md':2098, 'pu':115, 'rot':83, 'so':95, 'tq':16.0},
            {'md':2127, 'pu':118, 'rot':83, 'so':95, 'tq':17.0},
            {'md':2155, 'pu':119, 'rot':83, 'so':96, 'tq':18.0},
            {'md':2184, 'pu':120, 'rot':82, 'so':97, 'tq':18.0},
            {'md':2212, 'pu':119, 'rot':83, 'so':97, 'tq':18.0},
            {'md':2241, 'pu':120, 'rot':82, 'so':97, 'tq':18.0},
            {'md':2298, 'pu':122, 'rot':81, 'so':99, 'tq':18.0},
            {'md':2327, 'pu':121, 'rot':82, 'so':100, 'tq':17.0},
            {'md':2384, 'pu':123, 'rot':83, 'so':100, 'tq':18.0},
            {'md':2442, 'pu':125, 'rot':81, 'so':101, 'tq':18.0},
            {'md':2470, 'pu':126, 'rot':82, 'so':103, 'tq':19.0},
            {'md':2499, 'pu':128, 'rot':82, 'so':103, 'tq':18.0},
            {'md':2528, 'pu':130, 'rot':80, 'so':102, 'tq':19.0},
            {'md':2556, 'pu':131, 'rot':82, 'so':102, 'tq':19.0},
            {'md':2585, 'pu':133, 'rot':82, 'so':102, 'tq':19.0},
            {'md':2614, 'pu':130, 'rot':83, 'so':100, 'tq':19.0},
            {'md':2642, 'pu':132, 'rot':84, 'so':101, 'tq':19.0},
            {'md':2671, 'pu':134, 'rot':83, 'so':102, 'tq':20.0},
            {'md':2700, 'pu':135, 'rot':84, 'so':102, 'tq':20.0},
            {'md':2728, 'pu':136, 'rot':84, 'so':102, 'tq':21.0},
            {'md':2757, 'pu':139, 'rot':84, 'so':103, 'tq':21.0},
            {'md':2786, 'pu':141, 'rot':84, 'so':103, 'tq':21.0},
            {'md':2843, 'pu':142, 'rot':84, 'so':105, 'tq':21.0},
            {'md':2872, 'pu':142, 'rot':85, 'so':106, 'tq':22.0},
            {'md':2901, 'pu':143, 'rot':84, 'so':107, 'tq':22.0},
            {'md':2958, 'pu':145, 'rot':86, 'so':107, 'tq':23.0},
            {'md':2987, 'pu':143, 'rot':87, 'so':107, 'tq':23.5},
            {'md':3015, 'pu':145, 'rot':87, 'so':107, 'tq':23.5},
            {'md':3044, 'pu':147, 'rot':87, 'so':107, 'tq':24.0},
            {'md':3073, 'pu':147, 'rot':87, 'so':105, 'tq':24.0},
            {'md':3101, 'pu':147, 'rot':87, 'so':108, 'tq':25.0},
            {'md':3130, 'pu':153, 'rot':86, 'so':108, 'tq':25.0},
            {'md':3159, 'pu':154, 'rot':87, 'so':108, 'tq':25.0},
            {'md':3187, 'pu':152, 'rot':86, 'so':109, 'tq':26.0},
            {'md':3216, 'pu':153, 'rot':85, 'so':109, 'tq':26.0},
            {'md':3245, 'pu':154, 'rot':85, 'so':110, 'tq':27.0},
            {'md':3277, 'pu':153, 'rot':85, 'so':110, 'tq':26.0},
            {'md':3302, 'pu':150, 'rot':85, 'so':111, 'tq':26.0},
            {'md':3331, 'pu':151, 'rot':83, 'so':111, 'tq':26.5},
            {'md':3359, 'pu':153, 'rot':83, 'so':107, 'tq':26.5},
            {'md':3373, 'pu':154, 'rot':83, 'so':110, 'tq':26.0},
            {'md':3388, 'pu':148, 'rot':84, 'so':110, 'tq':26.0},
            {'md':3417, 'pu':149, 'rot':84, 'so':111, 'tq':26.0},
            {'md':3445, 'pu':145, 'rot':85, 'so':109, 'tq':26.0}]