### Utility functions ###

# Decibel conversion lambda
dB = lambda x: 10 * np.log10(x)

# Linear conversion lambda
lin = lambda x: 10 ** (x / 10)


class RF:
    '''
    RF Link class
    
    Parameters
    ----------
    f           Carrier Frequency       Hz
    '''
    
    def __init__(self, f):
        self.frequency = f
    
    
    