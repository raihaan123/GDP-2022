import numpy as np

### Utility functions - will move somewhere better ###
dB = lambda x: 10 * np.log10(x)         # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)          # Linear conversion lambda

class Platform:
    '''
    Defines a general Platform - an Antenna is assigned a Platform
    '''

    def __init__(self):
        self.r_ecef = None


    def get_r_ecef(self):
        return self.r_ecef



class GroundStation:
    '''
    Defines a Ground Station


    Input Parameters
    ----------------
    lat         Latitude            deg
    lon         Longitude           deg
    alt         Altitude            m
    '''

    def __init__(self, lat, lon, alt):
        self.lat = lat
        self.lon = lon
        self.alt = alt
        
        to_ecef()


    def to_ecef(self):
        '''
        Calculate the ground station position in ECEF coordinates
        '''
        # Convert lat, lon, alt to radians
        lat_rad = np.deg2rad(self.lat)
        lon_rad = np.deg2rad(self.lon)
        
        self.r_ecef = np.array([
            self.alt * np.cos(lat_rad) * np.cos(lon_rad),
            self.alt * np.cos(lat_rad) * np.sin(lon_rad),
            self.alt * np.sin(lat_rad)
        ])



class Satellite(Platform):
    '''
    Satellite base class

    Parameters
    ----------
    a           Semi-major axis             m
    e           Eccentricity                -
    i           Inclination                 deg
    RAAN        Right ascension             deg
    w           Argument of perigee         deg
    M           Mean anomaly                deg
    T0          Epoch                       -
    '''

    def __init__(self, a, e, i, RAAN, w, M, T0):
        None



class GEORelay(Satellite):
    '''
    Geostationary Relay satellite class - r_ecef is approximately fixed
    
    Parameters
    ----------
    r_ecef     Satellite position in ECEF frame
    '''
    
    def __init__(self, r_ecef):
        self.r_ecef = r_ecef
