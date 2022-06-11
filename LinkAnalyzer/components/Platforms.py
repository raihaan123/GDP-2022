import numpy as np
import pygeodesy as geo

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
        self.lat = np.deg2rad(lat)
        self.lon = np.deg2rad(lon)
        self.alt = alt
        
        self.to_ecef()


    def to_ecef(self):
        '''
        Calculate the ground station position in ECEF coordinates
        '''
        lat = self.lat
        lon = self.lon
        
        # convert LLA to ECEF with the following equations
        cos_lat = np.cos(lat)
        cos_lon = np.cos(lon)
        sin_lat = np.sin(lat)

        A = 6378137
        B = 6356752.31424518
        H = self.alt
        E1 = np.sqrt((A**2-B**2)/A**2)
        E2 = E1**2
        N = A/np.sqrt(1-E2*(sin_lat**2))

        self.r_ecef = [(N+H)*cos_lat*cos_lon,
                     (N+H)*cos_lat*np.sin(lon),
                     (N*(1-E2)+H)*sin_lat]



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
