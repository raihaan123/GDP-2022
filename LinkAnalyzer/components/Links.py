import numpy as np

### Utility functions - will move somewhere better ###
dB = lambda x: 10 * np.log10(x)         # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)          # Linear conversion lambda
pi = np.pi                              # Good old pi
c = 299792458                           # Speed of light


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
        self.FSPL = 2 * ( dB(self.d) + dB(self.frequency) + dB(4*pi / c) )
        self.calculate_L_atm()
        
        self.L_rx_chain = self.RX.L_line + self.FSPL + self.L_atm
        self.L_total = self.L_rx_chain + self.TX.L_line

        # Compute antenna gains
        self.TX.set_gain(self.frequency)
        self.RX.set_gain(self.frequency)
        
        # Calculate signal to noise ratio
        self.calculate_eb_n0()



    def calculate_L_atm(self):
        '''Calculate the atmospheric loss - extend this!!!'''
        self.L_atm = 10



    def calculate_eb_n0(self):
        '''Calculate Signal To Noise ratio'''

        # Receiver gain to noise temperature ratio
        self.G_T = self.RX.G - dB(self.Ts)

        # Received signal power to noise power ratio
        self.C_N0 = self.TX.EIRP + self.G_T - self.L_rx_chain + 228.6

        # Signal To Noise ratio
        self.Eb_N0 = self.C_N0 - dB(self.Rb)



    def report(self):
        '''Print the link budget'''

        print(f'EIRP:   {self.TX.EIRP:.2f} dB\n\
                FSPL:   {self.FSPL:.2f} dB\n\
                G_tx:   {self.TX.G:.2f} dB\n\
                G_rx:   {self.RX.G:.2f} dB\n\
                G_t:    {self.G_T:.2f} dB\n\
                C_n0:   {self.C_N0:.2f} dB\n\
                Eb_n0:  {self.Eb_N0:.2f} dB')
