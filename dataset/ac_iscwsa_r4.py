from dataset.units import units


task = {
  "units": units,
  "well1": {
        "name": "string",
        "head": {"ns": 0, "ew": 0, "tvd": 0},
        "stations": [{'md':0, 'inc':0.00, 'az':0.00},
                    {'md':1, 'inc':0.00, 'az':0.00},
                    {'md':30, 'inc':0.00, 'az':0.00},
                    {'md':60, 'inc':0.00, 'az':0.00},
                    {'md':90, 'inc':0.00, 'az':0.00},
                    {'md':120, 'inc':0.00, 'az':0.00},
                    {'md':150, 'inc':0.00, 'az':0.00},
                    {'md':180, 'inc':0.00, 'az':0.00},
                    {'md':210, 'inc':0.00, 'az':0.00},
                    {'md':240, 'inc':0.00, 'az':0.00},
                    {'md':270, 'inc':0.00, 'az':0.00},
                    {'md':300, 'inc':0.00, 'az':0.00},
                    {'md':330, 'inc':0.00, 'az':0.00},
                    {'md':360, 'inc':0.00, 'az':0.00},
                    {'md':390, 'inc':0.00, 'az':0.00},
                    {'md':420, 'inc':0.00, 'az':0.00},
                    {'md':450, 'inc':0.00, 'az':0.00},
                    {'md':480, 'inc':0.00, 'az':0.00},
                    {'md':510, 'inc':0.00, 'az':0.00},
                    {'md':540, 'inc':0.00, 'az':0.00},
                    {'md':570, 'inc':0.00, 'az':0.00},
                    {'md':600, 'inc':0.00, 'az':0.00},
                    {'md':630, 'inc':0.00, 'az':0.00},
                    {'md':660, 'inc':0.00, 'az':0.00},
                    {'md':690, 'inc':0.00, 'az':0.00},
                    {'md':720, 'inc':0.00, 'az':0.00},
                    {'md':750, 'inc':0.00, 'az':0.00},
                    {'md':780, 'inc':0.00, 'az':0.00},
                    {'md':810, 'inc':0.00, 'az':0.00},
                    {'md':840, 'inc':0.00, 'az':0.00},
                    {'md':870, 'inc':0.00, 'az':0.00},
                    {'md':900, 'inc':0.00, 'az':0.00},
                    {'md':930, 'inc':0.00, 'az':0.00},
                    {'md':960, 'inc':0.00, 'az':0.00},
                    {'md':990, 'inc':0.00, 'az':0.00},
                    {'md':1020, 'inc':1.33, 'az':180.00},
                    {'md':1050, 'inc':3.33, 'az':180.00},
                    {'md':1080, 'inc':5.33, 'az':180.00},
                    {'md':1110, 'inc':7.33, 'az':180.00},
                    {'md':1140, 'inc':9.33, 'az':180.00},
                    {'md':1170, 'inc':11.33, 'az':180.00},
                    {'md':1200, 'inc':13.33, 'az':180.00},
                    {'md':1230, 'inc':15.33, 'az':180.00},
                    {'md':1260, 'inc':17.33, 'az':180.00},
                    {'md':1290, 'inc':19.33, 'az':180.00},
                    {'md':1320, 'inc':21.33, 'az':180.00},
                    {'md':1350, 'inc':23.33, 'az':180.00},
                    {'md':1380, 'inc':25.33, 'az':180.00},
                    {'md':1410, 'inc':27.33, 'az':180.00},
                    {'md':1440, 'inc':29.33, 'az':180.00},
                    {'md':1470, 'inc':31.33, 'az':180.00},
                    {'md':1500, 'inc':33.33, 'az':180.00},
                    {'md':1530, 'inc':35.33, 'az':180.00},
                    {'md':1560, 'inc':37.33, 'az':180.00},
                    {'md':1590, 'inc':39.33, 'az':180.00},
                    {'md':1620, 'inc':41.33, 'az':180.00},
                    {'md':1650, 'inc':43.33, 'az':180.00},
                    {'md':1680, 'inc':45.33, 'az':180.00},
                    {'md':1710, 'inc':47.33, 'az':180.00},
                    {'md':1740, 'inc':49.33, 'az':180.00},
                    {'md':1770, 'inc':51.33, 'az':180.00},
                    {'md':1800, 'inc':53.33, 'az':180.00},
                    {'md':1830, 'inc':55.33, 'az':180.00},
                    {'md':1860, 'inc':57.33, 'az':180.00},
                    {'md':1890, 'inc':59.33, 'az':180.00},
                    {'md':1920, 'inc':61.33, 'az':180.00},
                    {'md':1950, 'inc':63.33, 'az':180.00},
                    {'md':1980, 'inc':65.33, 'az':180.00},
                    {'md':2010, 'inc':67.33, 'az':180.00},
                    {'md':2040, 'inc':69.33, 'az':180.00},
                    {'md':2070, 'inc':71.33, 'az':180.00},
                    {'md':2100, 'inc':73.33, 'az':180.00},
                    {'md':2130, 'inc':75.33, 'az':180.00},
                    {'md':2160, 'inc':77.33, 'az':180.00},
                    {'md':2190, 'inc':79.33, 'az':180.00},
                    {'md':2220, 'inc':81.33, 'az':180.00},
                    {'md':2250, 'inc':83.33, 'az':180.00},
                    {'md':2280, 'inc':85.00, 'az':180.00},
                    {'md':2310, 'inc':85.00, 'az':180.00},
                    {'md':2340, 'inc':85.00, 'az':180.00},
                    {'md':2370, 'inc':85.00, 'az':180.00},
                    {'md':2400, 'inc':85.00, 'az':180.00},
                    {'md':2430, 'inc':85.00, 'az':180.00},
                    {'md':2460, 'inc':85.00, 'az':180.00},
                    {'md':2490, 'inc':85.00, 'az':180.00},
                    {'md':2520, 'inc':85.00, 'az':180.00},
                    {'md':2550, 'inc':85.00, 'az':180.00},
                    {'md':2580, 'inc':85.00, 'az':180.00},
                    {'md':2610, 'inc':85.00, 'az':180.00},
                    {'md':2640, 'inc':85.00, 'az':180.00},
                    {'md':2670, 'inc':85.00, 'az':180.00},
                    {'md':2700, 'inc':85.00, 'az':180.00},
                    {'md':2730, 'inc':85.00, 'az':180.00},
                    {'md':2760, 'inc':85.00, 'az':180.00},
                    {'md':2790, 'inc':86.00, 'az':180.00},
                    {'md':2820, 'inc':88.00, 'az':180.00},
                    {'md':2850, 'inc':90.00, 'az':180.00},
                    {'md':2880, 'inc':90.00, 'az':180.00},
                    {'md':2910, 'inc':90.00, 'az':180.00},
                    {'md':2940, 'inc':90.00, 'az':180.00}],
        "surveyProgram": [
            {"depth": None, "toolcode": "MWD"}
        ],
        "reference": {"lat": 0, "lon": 0, "alt": 0, "g": 9.80665, "b": 50000, "dip": 70, "dec": 0, "grid": 0},
        "slotUncertainty": {"ns": 0, "ew": 0, "tvd": 0},
        "outerDiameter": 0.9144
    },
  "well2": {
        "name": "string",
        "head": {"ns": 0, "ew": 10, "tvd": 0},
        "stations": [{'md':0, 'inc':0.00, 'az':0.00},
                    {'md':1, 'inc':0.00, 'az':0.00},
                    {'md':30, 'inc':0.00, 'az':0.00},
                    {'md':60, 'inc':0.00, 'az':0.00},
                    {'md':90, 'inc':0.00, 'az':0.00},
                    {'md':120, 'inc':0.00, 'az':0.00},
                    {'md':150, 'inc':0.00, 'az':0.00},
                    {'md':180, 'inc':0.00, 'az':0.00},
                    {'md':210, 'inc':0.00, 'az':0.00},
                    {'md':240, 'inc':0.00, 'az':0.00},
                    {'md':270, 'inc':0.00, 'az':0.00},
                    {'md':300, 'inc':0.00, 'az':0.00},
                    {'md':330, 'inc':0.00, 'az':0.00},
                    {'md':360, 'inc':0.00, 'az':0.00},
                    {'md':390, 'inc':0.00, 'az':0.00},
                    {'md':420, 'inc':0.00, 'az':0.00},
                    {'md':450, 'inc':0.00, 'az':0.00},
                    {'md':480, 'inc':0.00, 'az':0.00},
                    {'md':510, 'inc':0.00, 'az':0.00},
                    {'md':540, 'inc':0.00, 'az':0.00},
                    {'md':570, 'inc':0.00, 'az':0.00},
                    {'md':600, 'inc':0.00, 'az':0.00},
                    {'md':630, 'inc':0.00, 'az':0.00},
                    {'md':660, 'inc':0.00, 'az':0.00},
                    {'md':690, 'inc':0.00, 'az':0.00},
                    {'md':720, 'inc':0.00, 'az':0.00},
                    {'md':750, 'inc':0.00, 'az':0.00},
                    {'md':780, 'inc':0.00, 'az':0.00},
                    {'md':810, 'inc':0.00, 'az':0.00},
                    {'md':840, 'inc':0.00, 'az':0.00},
                    {'md':870, 'inc':0.00, 'az':0.00},
                    {'md':900, 'inc':0.00, 'az':0.00},
                    {'md':930, 'inc':0.00, 'az':0.00},
                    {'md':960, 'inc':0.00, 'az':0.00},
                    {'md':990, 'inc':0.00, 'az':0.00},
                    {'md':1020, 'inc':1.33, 'az':175.00},
                    {'md':1050, 'inc':3.33, 'az':175.00},
                    {'md':1080, 'inc':5.33, 'az':175.00},
                    {'md':1110, 'inc':7.33, 'az':175.00},
                    {'md':1140, 'inc':9.33, 'az':175.00},
                    {'md':1170, 'inc':11.33, 'az':175.00},
                    {'md':1200, 'inc':13.33, 'az':175.00},
                    {'md':1230, 'inc':15.33, 'az':175.00},
                    {'md':1260, 'inc':17.33, 'az':175.00},
                    {'md':1290, 'inc':19.33, 'az':175.00},
                    {'md':1320, 'inc':21.33, 'az':175.00},
                    {'md':1350, 'inc':23.33, 'az':175.00},
                    {'md':1380, 'inc':25.33, 'az':175.00},
                    {'md':1410, 'inc':27.33, 'az':175.00},
                    {'md':1440, 'inc':29.33, 'az':175.00},
                    {'md':1470, 'inc':31.33, 'az':175.00},
                    {'md':1500, 'inc':33.33, 'az':175.00},
                    {'md':1530, 'inc':35.33, 'az':175.00},
                    {'md':1560, 'inc':37.33, 'az':175.00},
                    {'md':1590, 'inc':39.33, 'az':175.00},
                    {'md':1620, 'inc':41.33, 'az':175.00},
                    {'md':1650, 'inc':43.33, 'az':175.00},
                    {'md':1680, 'inc':45.31, 'az':175.18},
                    {'md':1710, 'inc':47.16, 'az':176.22},
                    {'md':1740, 'inc':49.02, 'az':177.21},
                    {'md':1770, 'inc':50.89, 'az':178.13},
                    {'md':1800, 'inc':52.77, 'az':179.02},
                    {'md':1830, 'inc':54.65, 'az':179.85},
                    {'md':1860, 'inc':56.54, 'az':180.65},
                    {'md':1890, 'inc':58.43, 'az':181.42},
                    {'md':1920, 'inc':60.33, 'az':182.15},
                    {'md':1950, 'inc':62.23, 'az':182.86},
                    {'md':1980, 'inc':64.14, 'az':183.54},
                    {'md':2010, 'inc':66.04, 'az':184.20},
                    {'md':2040, 'inc':67.95, 'az':184.85},
                    {'md':2070, 'inc':69.87, 'az':185.47},
                    {'md':2100, 'inc':71.78, 'az':186.08},
                    {'md':2130, 'inc':73.70, 'az':186.68},
                    {'md':2160, 'inc':75.62, 'az':187.26},
                    {'md':2190, 'inc':77.54, 'az':187.84},
                    {'md':2220, 'inc':79.46, 'az':188.40},
                    {'md':2250, 'inc':81.38, 'az':188.96},
                    {'md':2280, 'inc':83.31, 'az':189.52},
                    {'md':2310, 'inc':85.00, 'az':190.00},
                    {'md':2340, 'inc':85.00, 'az':190.00},
                    {'md':2370, 'inc':85.00, 'az':190.00},
                    {'md':2400, 'inc':85.00, 'az':190.00},
                    {'md':2430, 'inc':85.00, 'az':190.00},
                    {'md':2460, 'inc':85.00, 'az':190.00},
                    {'md':2490, 'inc':85.00, 'az':190.00},
                    {'md':2520, 'inc':85.00, 'az':190.00},
                    {'md':2550, 'inc':85.00, 'az':190.00},
                    {'md':2580, 'inc':85.00, 'az':190.00},
                    {'md':2610, 'inc':85.00, 'az':190.00},
                    {'md':2640, 'inc':85.00, 'az':190.00},
                    {'md':2670, 'inc':85.00, 'az':190.00},
                    {'md':2700, 'inc':85.00, 'az':190.00},
                    {'md':2730, 'inc':85.00, 'az':190.00},
                    {'md':2760, 'inc':85.00, 'az':190.00},
                    {'md':2790, 'inc':85.00, 'az':190.00},
                    {'md':2820, 'inc':85.00, 'az':190.00}],
        "surveyProgram": [
            {"depth": None, "toolcode": "MWD"}
        ],
        "reference": {"lat": 0, "lon": 0, "alt": 0, "g": 9.80665, "b": 50000, "dip": 70, "dec": 0, "grid": 0},
        "slotUncertainty": {"ns": 0, "ew": 0, "tvd": 0},
        "outerDiameter": 0.6096
    },
  "sigma": 3.5,
  "mdStep": 30
}

ac_benchmark =[{'md':0.0000, 'ctc':10.0000, 'osf':5.1074},
                {'md':1.0000, 'ctc':10.0000, 'osf':5.1074},
                {'md':30.0000, 'ctc':10.0000, 'osf':5.0495},
                {'md':60.0000, 'ctc':10.0000, 'osf':4.8869},
                {'md':90.0000, 'ctc':10.0000, 'osf':4.6472},
                {'md':120.0000, 'ctc':10.0000, 'osf':4.3639},
                {'md':150.0000, 'ctc':10.0000, 'osf':4.0658},
                {'md':180.0000, 'ctc':10.0000, 'osf':3.7734},
                {'md':210.0000, 'ctc':10.0000, 'osf':3.4973},
                {'md':240.0000, 'ctc':10.0000, 'osf':3.2433},
                {'md':270.0000, 'ctc':10.0000, 'osf':3.0135},
                {'md':300.0000, 'ctc':10.0000, 'osf':2.8064},
                {'md':330.0000, 'ctc':10.0000, 'osf':2.6207},
                {'md':360.0000, 'ctc':10.0000, 'osf':2.4544},
                {'md':390.0000, 'ctc':10.0000, 'osf':2.3055},
                {'md':420.0000, 'ctc':10.0000, 'osf':2.1714},
                {'md':450.0000, 'ctc':10.0000, 'osf':2.0506},
                {'md':480.0000, 'ctc':10.0000, 'osf':1.9416},
                {'md':510.0000, 'ctc':10.0000, 'osf':1.8426},
                {'md':540.0000, 'ctc':10.0000, 'osf':1.7526},
                {'md':570.0000, 'ctc':10.0000, 'osf':1.6704},
                {'md':600.0000, 'ctc':10.0000, 'osf':1.5953},
                {'md':630.0000, 'ctc':10.0000, 'osf':1.5262},
                {'md':660.0000, 'ctc':10.0000, 'osf':1.4626},
                {'md':690.0000, 'ctc':10.0000, 'osf':1.4040},
                {'md':720.0000, 'ctc':10.0000, 'osf':1.3496},
                {'md':750.0000, 'ctc':10.0000, 'osf':1.2992},
                {'md':780.0000, 'ctc':10.0000, 'osf':1.2523},
                {'md':810.0000, 'ctc':10.0000, 'osf':1.2086},
                {'md':840.0000, 'ctc':10.0000, 'osf':1.1677},
                {'md':870.0000, 'ctc':10.0000, 'osf':1.1294},
                {'md':900.0000, 'ctc':10.0000, 'osf':1.0935},
                {'md':930.0000, 'ctc':10.0000, 'osf':1.0598},
                {'md':960.0000, 'ctc':10.0000, 'osf':1.0280},
                {'md':990.0000, 'ctc':10.0000, 'osf':0.9981},
                {'md':1020.0000, 'ctc':10.0300, 'osf':0.9745},
                {'md':1050.0000, 'ctc':10.1400, 'osf':0.9620},
                {'md':1080.0000, 'ctc':10.3300, 'osf':0.9582},
                {'md':1110.0000, 'ctc':10.6200, 'osf':0.9644},
                {'md':1140.0000, 'ctc':11.0000, 'osf':0.9789},
                {'md':1170.0000, 'ctc':11.4700, 'osf':1.0007},
                {'md':1200.0000, 'ctc':12.0300, 'osf':1.0290},
                {'md':1230.0000, 'ctc':12.6700, 'osf':1.0622},
                {'md':1260.0000, 'ctc':13.4100, 'osf':1.1012},
                {'md':1290.0000, 'ctc':14.2300, 'osf':1.1433},
                {'md':1320.0000, 'ctc':15.1400, 'osf':1.1887},
                {'md':1350.0000, 'ctc':16.1300, 'osf':1.2357},
                {'md':1380.0000, 'ctc':17.2100, 'osf':1.2844},
                {'md':1410.0000, 'ctc':18.3700, 'osf':1.3332},
                {'md':1440.0000, 'ctc':19.6100, 'osf':1.3814},
                {'md':1470.0000, 'ctc':20.9300, 'osf':1.4285},
                {'md':1500.0000, 'ctc':22.3200, 'osf':1.4734},
                {'md':1530.0000, 'ctc':23.8000, 'osf':1.5172},
                {'md':1560.0000, 'ctc':25.3500, 'osf':1.5581},
                {'md':1590.0000, 'ctc':26.9700, 'osf':1.5962},
                {'md':1620.0000, 'ctc':28.6600, 'osf':1.6315},
                {'md':1650.0000, 'ctc':30.4200, 'osf':1.6639},
                {'md':1680.0000, 'ctc':32.2100, 'osf':1.6913},
                {'md':1710.0000, 'ctc':33.8500, 'osf':1.7043},
                {'md':1740.0000, 'ctc':35.1400, 'osf':1.6953},
                {'md':1770.0000, 'ctc':36.0800, 'osf':1.6675},
                {'md':1800.0000, 'ctc':36.6700, 'osf':1.6233},
                {'md':1830.0000, 'ctc':36.9100, 'osf':1.5653},
                {'md':1860.0000, 'ctc':36.8000, 'osf':1.4955},
                {'md':1890.0000, 'ctc':36.3500, 'osf':1.4162},
                {'md':1920.0000, 'ctc':35.5500, 'osf':1.3288},
                {'md':1950.0000, 'ctc':34.4200, 'osf':1.2353},
                {'md':1980.0000, 'ctc':32.9500, 'osf':1.1366},
                {'md':2010.0000, 'ctc':31.1600, 'osf':1.0346},
                {'md':2040.0000, 'ctc':29.0700, 'osf':0.9310},
                {'md':2070.0000, 'ctc':26.6800, 'osf':0.8266},
                {'md':2100.0000, 'ctc':24.0400, 'osf':0.7241},
                {'md':2130.0000, 'ctc':21.1900, 'osf':0.6261},
                {'md':2160.0000, 'ctc':18.2300, 'osf':0.5382},
                {'md':2190.0000, 'ctc':15.3400, 'osf':0.4718},
                {'md':2220.0000, 'ctc':12.8700, 'osf':0.4566},
                {'md':2250.0000, 'ctc':11.4800, 'osf':0.5754},
                {'md':2280.0000, 'ctc':11.8500, 'osf':0.6743},
                {'md':2310.0000, 'ctc':13.7600, 'osf':0.5172},
                {'md':2340.0000, 'ctc':16.9000, 'osf':0.4883},
                {'md':2370.0000, 'ctc':20.8700, 'osf':0.5275},
                {'md':2400.0000, 'ctc':25.2900, 'osf':0.5907},
                {'md':2430.0000, 'ctc':29.9600, 'osf':0.6626},
                {'md':2460.0000, 'ctc':34.7700, 'osf':0.7368},
                {'md':2490.0000, 'ctc':39.6800, 'osf':0.8110},
                {'md':2520.0000, 'ctc':44.6600, 'osf':0.8838},
                {'md':2550.0000, 'ctc':49.6700, 'osf':0.9542},
                {'md':2580.0000, 'ctc':54.7200, 'osf':1.0223},
                {'md':2610.0000, 'ctc':59.8000, 'osf':1.0879},
                {'md':2640.0000, 'ctc':64.8900, 'osf':1.1507},
                {'md':2670.0000, 'ctc':70.0000, 'osf':1.2111},
                {'md':2700.0000, 'ctc':75.1100, 'osf':1.2689},
                {'md':2730.0000, 'ctc':80.2400, 'osf':1.3244},
                {'md':2760.0000, 'ctc':85.3700, 'osf':1.3775},
                {'md':2790.0000, 'ctc':90.5500, 'osf':1.4296},
                {'md':2820.0000, 'ctc':95.8400, 'osf':1.4825},
                {'md':2850.0000, 'ctc':104.9100, 'osf':1.7165},
                {'md':2880.0000, 'ctc':120.9800, 'osf':2.2014},
                {'md':2910.0000, 'ctc':141.6500, 'osf':2.8978},
                {'md':2940.0000, 'ctc':165.2100, 'osf':3.7723}]