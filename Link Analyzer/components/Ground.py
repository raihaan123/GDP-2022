import numpy as np

### Utility functions - will move somewhere better ###
dB = lambda x: 10 * np.log10(x)         # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)          # Linear conversion lambda


class GroundStation:
    '''
    The Ground Station class
    
    Contains the following models:
    - Antenna()
    
    
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
        
        
    def set_antenna(self, antenna):
        '''
        Set the antenna of the ground station
        '''
        
        self.antenna = antenna
