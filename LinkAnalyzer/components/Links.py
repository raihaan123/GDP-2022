import numpy as np
from .utils import dB, lin, pi, c


class RF:
    '''
    RF Link class

    Contains the following models:
    - Tx Antenna()
    - Rx Antenna()

    Parameters
    ----------
    Ts              System Temperature              K
    '''

    def __init__(self, TX, RX, Ts=525):
        
        # TX and RX Antenna objects are passed in
        self.TX = TX
        self.RX = RX
        
        self.Ts = Ts



    def compute(self, f, P_tx, Rb, L_line_tx, L_line_rx, mod=None, m=1):
        '''
        Calculate the link budget!
        
        Parameters
        ----------
        f               Carrier Frequency           Hz
        P_tx            Transmit Power              W
        Rb              Bit Rate                    bits/s
        L_line_tx       Transmit Line Loss          dB
        L_line_rx       Receive Line Loss           dB
        m               Code Rate                   -
        mod             Modulation Scheme           -       
        '''
        
        # Signal parameters
        self.f = f
        self.mod = mod
        self.m = m
        
        # Data parameters
        self.Rb = Rb

        # Assign parameters to the two antennas
        self.TX.set_operating_params(L_line_tx, frequency=f, power=P_tx)
        self.RX.set_operating_params(L_line_rx, frequency=f)

        # Path distance - take modulus of the difference of the two antenna positions
        d = self.d = np.linalg.norm(self.TX.platform.r_ecef - self.RX.platform.r_ecef)

        # Total system losses - free space, atmospheric, and line losses
        FSPL = self.FSPL = 2 * ( dB(d) + dB(f) + dB(4*pi / c) )
        L_atm = self.L_atm = self.calculate_L_atm()

        self.L_rx_chain = L_line_rx + FSPL + L_atm
        self.L_total = self.L_rx_chain + L_line_tx

        # Compute antenna gains
        self.TX.calculate()
        self.RX.calculate()
        
        # Calculate signal to noise ratio
        self.calculate_eb_n0()



    def calculate_L_atm(self):
        '''Calculate the atmospheric loss - extend this!!!'''
        return 10



    def calculate_eb_n0(self):
        '''Calculate Signal to Noise ratio'''

        # Receiver gain to noise temperature ratio
        self.G_T = self.RX.G - dB(self.Ts)

        # Received signal power to noise power ratio
        self.C_N0 = self.TX.EIRP + self.G_T - self.L_rx_chain + 228.6

        # Signal To Noise ratio
        self.Eb_N0 = self.C_N0 - dB(self.Rb)



    def report(self):
        '''Print the link budget'''

        print(f'Link Budget Report\n\
                Frequency:      {self.f} Hz\n\
                Path Distance:  {self.d} m\n\
                EIRP:           {self.TX.EIRP:.2f} dBW\n\
                FSPL:           {self.FSPL:.2f} dB\n\
                G_tx:           {self.TX.G:.2f} dBi\n\
                G_rx:           {self.RX.G:.2f} dBi\n\
                G/T:            {self.G_T:.2f} dB/K\n\
                C/N0:           {self.C_N0:.2f} dB-Hz\n\
                Eb/n0:          {self.Eb_N0:.2f} dB')

