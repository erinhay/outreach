import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact
from astropy import units as u

def model(times, period = 10, R_p = 0, R_star = 696_340, a = 1.5e8, offset=0, error=False):
    """
    Model adapted from Mandel & Agol 2002. Reparameterized to take 4 inputs: period of exoplanet orbit, radius of exoplanet, 
    radius of host star, and orbital radius.
    ---
    
    period (period of exoplanet orbit) given in units of days, defaults to 10 days
    
    R_p (radius of exoplanet) given in units of km, defaults to 0 km (no transit)
    
    R_star (radius of host star) given in units of km, defaults to 1 solar radius
    
    a (orbital radius) given in units of km, defaults to 1 AU
    """
    rate = 2*np.pi*a / period #km / day
    s = rate * (times+offset) #(km / day) * days = km
    d = a * (1 - np.cos(s / a)) #km

    p = R_p/R_star
    zs = d/R_star

    lamdba = np.zeros(len(zs))
    for i, z in enumerate(zs):
        if z > 1+p:
            lamdba[i] = 0
        elif z > np.abs(1-p) and z <= 1+p:
            k0 = np.arccos((p**2 + z**2 - 1)/(2*p*z))
            k1 = np.arccos((1 - p**2 + z**2)/(2*z))
            root = ((2*z)**2 - (1 + z**2 - p**2)**2) / 4
            lamdba[i] = ((k0 * p**2) + k1 - np.sqrt(root)) / np.pi
        elif z <= 1-p:
            lamdba[i] = p**2
        elif z <= p-1:
            lamdba[i] = 1
    
    brightness = np.ones(len(zs)) - lamdba
    if error:
        error_scale = 0.00005
        brightness += np.random.normal(0, error_scale, len(zs))
        error = np.repeat(error_scale, len(zs))
        return brightness, error

    return brightness


