### Utility functions ###
import numpy as np

dB  = lambda x: 10 * np.log10(x)            # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)              # Linear conversion lambda
pi  = np.pi                                 # Good old pi
c   = 299792458                             # Speed of light