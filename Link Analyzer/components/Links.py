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
        
        self.Ts = Ts
        self.m = m
        self.mod = mod
        self.Rb = Rb
   

    def compute(self):
        # Path distance - take modulus of the difference of the two antenna positions
        self.d = np.linalg.norm(self.TX.platform.r_ecef - self.RX.platform.r_ecef)
        
        # Total system losses
        self.calculate_fspl()
        self.calculate_L_atm()
        
        self.L_total_rx = self.RX.L_line + self.FSPL + self.L_atm
        self.L_total = self.L_total_rx + self.TX.L_line

        # Compute components in the Link Budget
        self.calculate_g_tx()
        self.calculate_g_rx()
        self.calculate_g_t()
        self.calculate_c()
        self.calculate_c_n0()
        self.calculate_eb_n0()


    def calculate_fspl(self):
        '''Free space path loss - in dB'''
        c = 299792458
        self.FSPL = 2 * ( dB(self.d) + dB(self.frequency) + dB(4*pi / c) )
        
        
    def calculate_L_atm(self):
        self.L_atm = 10


    def calculate_g_tx(self):
        '''Transmit antenna gain - call works for all antenna types'''
        self.TX.set_gain(self.frequency)


    def calculate_g_rx(self):
        '''Receive antenna gain - call works for all antenna types'''
        self.RX.set_gain(self.frequency)


    def calculate_g_t(self):
        '''Receiver gain to noise temperature ratio - both in dB'''
        self.G_T = self.RX.G - dB(self.Ts)
        
        
    def calculate_c(self):
        '''Calculate the link capacity'''
        self.C = self.TX.EIRP + self.RX.G - self.L_total_rx


    def calculate_c_n0(self):
        '''Received signal power to noise power ratio - both in dB'''
        self.C_N0 = self.TX.EIRP + self.G_T - self.L_total_rx + 228.6


    def calculate_eb_n0(self):
        '''Signal To Noise ratio'''
        self.Eb_N0 = self.C_N0 - dB(self.Rb)

    
    def report(self):
        '''Print the link budget'''
        print('EIRP:',  self.TX.EIRP)
        print('FSPL:',  self.FSPL)
        print('G_tx:',  self.TX.G)
        print('G_rx:',  self.RX.G)
        print('G_t:',   self.G_T)
        print('C:',     self.C)
        print('C_n0:',  self.C_N0)
        print('EB_n0:', self.Eb_N0)