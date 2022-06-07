import numpy as np

### Utility functions - will move somewhere better ###
dB = lambda x: 10 * np.log10(x)         # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)          # Linear conversion lambda


class Satellite:
    '''
    Satellite base class
    
    Contains the following models:
    - Antenna()
    - Power()
    
    Input Parameters
    ----------------
    
    '''