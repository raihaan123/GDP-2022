import numpy as np

from components import *

### Utility functions - will move somewhere better ###
dB = lambda x: 10 * np.log10(x)         # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)          # Linear conversion lambda


# Create a ground station object
gs = GroundStation(lat=0, lon=0, alt=0)

# Create a Geostationary satellite object
geo = GEORelay(r_ecef=gs.r_ecef + np.array([3.8e7, 0, 0]))



''' Uplink Sample '''

# Create an antenna object for the ground station
gs_antenna = Antenna(D=10, P=200, eta=0.55, L_line=4, platform=gs)

# Create an antenna object for the satellite
geo_antenna = ShapedAntenna(eta=0.7, L_line=2, platform=geo)

# Create a link object between the generated antennas
uplink = RF(f=14e9, TX=gs_antenna, RX=geo_antenna, Rb=44e6)

uplink.compute()
uplink.report()



'''Downlink Sample '''

# geo_antenna.set_power(power=100)