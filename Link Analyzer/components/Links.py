import numpy as np

### Utility functions - will move somewhere better ###
dB = lambda x: 10 * np.log10(x)         # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)          # Linear conversion lambda
pi = np.pi                              # Good old pi


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

    def __init__(self, f, TX, RX, Ts=525, m=0, mod=None, Rb=0):
        self.frequency = f

        # TX and RX Antenna objects are passed in
        self.TX = TX
        self.RX = RX

        # Effective system noise temperature in K
        self.Ts = Ts
   

    def compute(self):
        # Path distance - take modulus of the difference of the two antenna positions
        self.d = np.linalg.norm(self.TX.platform.r_ecef - self.RX.platform.r_ecef)
        
        # Total line losses
        self.L_total = self.TX.L_line + self.RX.L_line
        
        # Compute components in the Link Budget
        self.calculate_fspl()
        self.calculate_g_tx()
        self.calculate_g_rx()
        self.calculate_g_t()
        self.calculate_c_n0()
        self.calculate_eb_n0()


    def calculate_fspl(self):
        '''Free space path loss - in dB'''
        c = 299792458
        self.FSPL = 2 * ( dB(self.d) + dB(self.frequency) + dB(4*pi / c) )


    def calculate_g_tx(self):
        '''Transmit antenna gain - call works for all antenna types'''
        self.TX.set_gain(self.frequency)


    def calculate_g_rx(self):
        '''Receive antenna gain - call works for all antenna types'''
        self.RX.set_gain(self.frequency)


    def calculate_g_t(self):
        '''Receiver gain to noise temperature ratio - both in dB'''
        self.G_T = self.RX.G - dB(self.Ts)


    def calculate_c_n0(self):
        '''Received signal power to noise power ratio - both in dB'''
        self.C_N0 = self.TX.EIRP + self.G_T - self.L_total + 228.6


    def calculate_eb_n0(self):
        '''Signal To Noise ratio'''
        self.Eb_N0 = self.C_N0 - dB(self.Rb)
