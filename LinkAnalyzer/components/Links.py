import numpy as np
from scipy.special import erfc, erfcinv
from decimal import Decimal
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
        self.active = False


    def compute(self, f, Bw, Rb, m, L_line_tx, L_line_rx, BER=0, P_tx=0):
        '''
        Calculate the link budget!

        Parameters
        ----------
        f               Carrier Frequency           Hz
        Bw              Bandwidth                   Hz
        Rb              Bit Rate                    bits/s
        m               Bits per Symbol             -
        L_line_tx       Transmit Line Loss          dB
        L_line_rx       Receive Line Loss           dB
        BER             Bit Error Rate              -
        P_tx            Transmit Power              dBm
        '''

        # Carrier signal parameters
        self.f      = f
        self.Bw     = Bw
        self.Rb     = Rb
        self.m      = m
        self.BER    = BER

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

        # Do the thing
        if self.TX.fixed_power:     self.calculate_eb_n0()
        else:                       self.calculate_P_tx()


    def calculate_L_atm(self):
        '''Calculate the atmospheric loss - extend this!!!'''
        return 10


    def Eb_N0_to_BER(self):
        ''' Convert Eb/N0 to BER '''

        m      = self.m
        M      = 2**m
        Eb_N0  = self.Eb_N0
        
        self.BER = erfc(np.sqrt(m*Eb_N0) * np.sin(pi/M)) / m        # 16-19


    def calculate_eb_n0(self):
        '''Calculate Signal to Noise ratio'''

        # Receiver gain to noise temperature ratio
        self.G_T = self.RX.G - dB(self.Ts)

        # Received signal power to noise power ratio
        self.C_N0 = self.TX.EIRP + self.G_T - self.L_rx_chain + 228.6

        # Signal To Noise ratio
        self.Eb_N0 = self.C_N0 - dB(self.Rb)
        
        # Convert Eb/N0 to BER
        self.Eb_N0_to_BER()


    def BER_to_Eb_N0(self):
        ''' Convert BER to Eb/N0 '''
        
        m       = self.m
        M       = 2**m
        BER     = self.BER
        
        self.Eb_N0 = (erfcinv(m*BER) / np.sin(pi/M)) ** 2 / m        # 16-19 rearranged


    def calculate_P_tx(self):
        ''' Calculate the transmit power needed '''
        
        # Convert BER to Eb/N0 using the specified modulation scheme
        self.BER_to_Eb_N0()
        
        # Rearranging to find P_tx required to achieve Eb/N0 and thus BER
        self.TX.EIRP  = self.Eb_N0 - self.RX.G + dB(self.Ts) + self.L_rx_chain - 228.6 + dB(self.Rb)
        self.TX.P     = self.TX.EIRP - self.TX.G + self.TX.L_line


    def report(self):
        '''Print the link budget'''

        print(f'Link Budget Report\n\
                Frequency:      {self.f} Hz\n\
                Path Distance:  {self.d} m\n\
                Power (W):      {self.TX.P} W\n\
                EIRP:           {self.TX.EIRP:.2f} dBW\n\
                FSPL:           {self.FSPL:.2f} dB\n\
                Eb/n0:          {self.Eb_N0:.2f} dB\n\
                BER:            {Decimal(self.BER):.2e}')
# print ber in scientific notation - use decimal.Decimal()
# print(f'BER:            {Decimal(self.BER):.2e}')

                # G_tx:           {self.TX.G:.2f} dBi\n\
                # G_rx:           {self.RX.G:.2f} dBi\n\
                # G/T:            {self.G_T:.2f} dB/K\n\
                # C/N0:           {self.C_N0:.2f} dB-Hz\n\