import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from ipywidgets import interact
from astropy import units as u
import astropy.cosmology.units as cu
from astropy.time import Time
from astropy.cosmology import FlatLambdaCDM
import sncosmo

H0 = 70.
Om0 = 0.3
cosmo = FlatLambdaCDM(H0=H0, Om0=Om0)

def read_data(fn):
    head, data = sncosmo.read_snana_ascii(fn, default_tablename='OBS')
    data = data['OBS']
    data = data[data['FLT'] == 'f160w']
    data.rename_column('MJD', 'time')
    data.rename_column('FLUXCAL', 'brightness')
    data.rename_column('FLUXCALERR', 'brightness_err')
    return head, data

def mjd_to_date(x, pos=None):
    return Time(x, format='mjd').to_value(format='iso', subfmt='date')

def normal_star(times):
    brightness = np.zeros(len(times))
    return brightness

def supernova(times, peak_brightness = 1000., color = 0., shape = 0., explosion_time = 30., redshift=1.25, filter = 'lssti', error=False):
    """
    Supernovae light curves from the SALT2 model as observed in a single band & parameterized by color, shape, explosion time, and distance.
    ---
    distance (comoving distance to the supernova): given in units of Mpc, defaults to 1000 Mpc
    
    color (light curve color parameter): unitless, defaults to 0
    
    shape (light curve shape parameter): unitless, defaults to 0
    
    explosion_time (time of peak supernova brightness): given in units of days, defaults to 15 days

    filter (filter of observations): unitless, defaults to Bessell B-band
    """

    # Retrieve the redshift corresponding to this distance in standard cosmology
    z_ref = redshift*cu.redshift
    d_ref = z_ref.to(u.Mpc, cu.redshift_distance(cosmo))
    baseline_model = sncosmo.Model('salt2')
    baseline_model.set(z=z_ref, t0=explosion_time, x1=0., c=0.)
    baseline_model.set_source_peakabsmag(-19.5, 'BessellB', 'ab')
    peak_ref = np.max(baseline_model.bandflux(filter, times, 27.5, 'ab'))

    # Define the supernova light curve model from SALT2
    supernova_model = sncosmo.Model('salt2')

    # Set properties of supernova model
    supernova_model.set(z=redshift, t0=explosion_time, x1=shape, c=color)
    supernova_model.set_source_peakabsmag(-19.5, 'BessellB', 'ab')

    # Get model brightnesses from the supernova model
    brightness_shape = supernova_model.bandflux(filter, times, 27.5, 'ab')

    brightness = brightness_shape * (peak_brightness / peak_ref)
    distance = d_ref * np.sqrt(peak_ref / peak_brightness)

    # Compute uncertainties if applicable
    if error:
        error_scale = 0.05*np.max(brightness)
        brightness += np.random.normal(0, error_scale, len(brightness))
        error = np.repeat(error_scale, len(brightness))
        return distance, brightness, error

    return distance, brightness