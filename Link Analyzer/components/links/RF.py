### Utility functions ###

# Decibel conversion lambda
dB = lambda x: 10 * np.log10(x)

# Linear conversion lambda
lin = lambda x: 10 ** (x / 10)


class RF:
    '''
    RF Link class
    
    Contains the following models:
    - Tx Antenna()
    - Rx Antenna()
    
    Parameters
    ----------
    f           Carrier Frequency       Hz
    '''
    
    def __init__(self, f, TX, RX):
        self.frequency = f
        
        self.TX = Antenna(D, P, eta)
        
    
    def calculate_FSPL(self, d):
        # Free space path loss - in dB
        c = 299792458
        self.FSPL = 2 * ( dB(d) + dB(self.frequency) + dB(4*pi / c) )
        
    
    def calculate_G_tx(self, A_theta=None):
        
    
    
    def calculate_C(self):
        # Received power - the sum of EIRP and G_rx and minus the FSPL, atmospheric and line losses
        self.C = eirp + G_rx - L_s - L_atm - L_line
    