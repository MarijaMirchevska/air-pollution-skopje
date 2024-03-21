def get_CO_subindex(x):
    '''Calculating the AQI for CO pollutant using the AQI Technical Assistance Document'''
    if x <= 4.4:
        return (50/4.4) * x
    elif x <= 9.4:
        return ((49/4.9) * (x-4.9)) + 51
    elif x <= 12.4:
        return (49/2.9) * (x-2.9) + 101
    elif x <= 15.4:
        return (49/2.9) * (x-2.9) + 151
    elif x <= 30.4:
        return (99/14.9) * (x-14.9) + 201
    elif x > 30.5 and x <= 50.4:
        return ((199/19.9) * (x-19.9)) + 301
    else:
        return 0
    
def get_NO2_subindex(x):
    '''Calculating the AQI for NO2 pollutant using the AQI Technical Assistance Document'''
    if x <= 53:
        return (50/53) * x
    elif x <= 100:
        return (49/46) * (x-54) + 51
    elif x <= 360:
        return (49/259) * (x-101) + 101
    elif x <= 649:
        return (49/288) * (x-361) + 151
    elif x <= 1249:
        return (99/599) * (x-650) + 201
    elif x > 1250 and x <= 2049:
        return (199/799) * (x-1250) + 301
    else:
        return 0    
    
def get_O3_subindex(x):
    '''Calculating the AQI for O3 pollutant using the AQI Technical Assistance Document'''
    if x <= 0.124:
        return 0
    elif x <= 0.164:
        return (49/0.039) * (x-0.125) + 101
    elif x <= 0.204:
        return (49/0.039) * (x-0.165) + 151
    elif x <= 0.404:
        return (99/0.199) * (x-0.205) + 201
    elif x > 0.405 and x <= 0.604:
        return (199/0.199) * (x-0.405) + 301
    else:
        return 0

def get_PM10_subindex(x):
    '''Calculating the AQI for PM10 pollutant using the AQI Technical Assistance Document'''
    if x <= 54:
        return (50/54) * x
    elif x <= 154:
        return (49/2.8) * (x-55) + 51
    elif x <= 254:
        return (49/99) * (x-155) + 101
    elif x <= 354:
        return (49/99) * (x-255) + 151
    elif x <= 424:
        return (99/69) * (x-355) + 201
    elif x > 425 and x <= 604:
        return (199/179) * (x-425) + 301
    else:
        return 0
    
def get_PM25_subindex(x):
    '''Calculating the AQI for PM25 pollutant using the AQI Technical Assistance Document'''
    if x <= 12:
        return (50/12) * x
    elif x <= 35.4:
        return (49/23.3) * (x-12.1) + 51
    elif x <= 55.4:
        return (49/19.9) * (x-35.5) + 101
    elif x <= 150.4:
        return (49/94.9) * (x-55.5) + 151
    elif x <= 250.4:
        return (99/99.9) * (x-150.5) + 201
    elif x > 250.5 and x <= 500.4:
        return (199/249.9) * (x-250.5) + 301
    else:
        return 0