import numpy as np

### Utility functions - will move somewhere better ###
dB = lambda x: 10 * np.log10(x)         # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)          # Linear conversion lambda


class RF:
    '''
    RF Link class
    
    Contains the following models:
    - Tx Antenna()
    - Rx Antenna()
    
    Parameters
    ----------
    f           Carrier Frequency       Hz
    m           Code Rate                -
    mod         Modulation Scheme        -
    '''
    
    def __init__(self, f, TX, RX):
        self.frequency = f
        
        # TX and RX Antenna objects are passed in
        self.TX = TX
        self.RX = RX
    
    
    def calculate_FSPL(self, d):
        # Free space path loss - in dB
        c = 299792458
        self.FSPL = 2 * ( dB(d) + dB(self.frequency) + dB(4*pi / c) )
        
    
    def calculate_G_tx(self):
        # Transmit antenna gain - call works for all antenna types
        self.TX.set_gain(self.frequency)
        
        
    def calculate_G_rx(self):
        # Receive antenna gain - call works for all antenna types
        self.RX.set_gain(self.frequency)
        
    
    def calculate_C(self):
        # Received power - the sum of EIRP and G_rx and minus the FSPL, atmospheric and line losses
        self.C = eirp + G_rx - L_s - L_atm - L_line
    


# # C/N0 - Received signal power to noise power ratio - both in dB
# C_N0 = lambda eirp, g_t, L_total: eirp + g_t - L_total + 228.6


# # Eb/N0 - Signal To Noise ratio
# Eb_N0 = lambda c_n0, Rb: c_n0 - dB(Rb)

    def calculate_G_T(self):
        # Receiver gain to noise temperature ratio - both in dB
        self.G_T = self.RX.G - self.RX.T