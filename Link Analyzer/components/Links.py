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
    f           Carrier Frequency        Hz
    m           Code Rate                -
    mod         Modulation Scheme        -
    Rb          Bit Rate                 bits/s
    '''

    def __init__(self, f, m, mod, Rb, TX, RX, Ts=525):
        self.frequency = f
        
        # TX and RX Antenna objects are passed in
        self.TX = TX
        self.RX = RX
        
        # Effective system noise temperature in K
        self.Ts = Ts

        # Path distance
        self.d = RX.platform.get_r_ecef() - TX.platform.get_r_ecef()


    def calculate_fspl(self, d):
        '''Free space path loss - in dB'''
        c = 299792458
        self.FSPL = 2 * ( dB(d) + dB(self.frequency) + dB(4*pi / c) )


    def calculate_g_tx(self):
        '''Transmit antenna gain - call works for all antenna types'''
        self.TX.set_gain(self.frequency)


    def calculate_g_rx(self):
        '''Receive antenna gain - call works for all antenna types'''
        self.RX.set_gain(self.frequency)


    def calculate_g_t(self):
        '''Receiver gain to noise temperature ratio - both in dB'''
        self.G_T = self.RX.G - dB(self.Ts)


    def calculate c_n0(self):
        '''Received signal power to noise power ratio - both in dB'''
        self.C_N0 = self.TX.EIRP + self.G_T - self.L_total + 228.6


    def calculate_eb_n0(self):
        '''Signal To Noise ratio'''
        self.Eb_N0 = self.C_N0 - dB(self.Rb)
