### Utility functions ###

# Decibel conversion lambda
dB = lambda x: 10 * np.log10(x)

# Linear conversion lambda
lin = lambda x: 10 ** (x / 10)


class GroundStation:
    '''
    The ground station class
    
    Contains the following models:
    - Antenna()
    
    
    Parameters
    ----------
    
    '''
    
    def __init__(self, D, P, eta):
        self.D = D
        self.P = P
        self.eta = eta
        
        self.beamwidth = 0
    
     
    def set_beamwidth(self, frequency):
        '''
        TX Antenna half-power beamwidth - in degrees
        Augumented for f in Hz, D in m
        '''
        
        self.beamwidth = 21e9 / (frequency * self.D)
        
        
    def set_power(self, power):
        '''
        Set the transmit power in W
        '''
        
        self.P = power


    def set_gain(self, frequency, A_theta=None):
        '''
        Antenna gain in dB - specific to antennas with a circularly symmetric radiating aperture
        Augumented for f in Hz, D in m
        '''
        
        if A_theta is None:
            self.G_tx = 200.4 + 2*dB(D) + 2*dB(frequency) + dB(eta)     

        else:
            # Beam shaping - directivity is a function of coverage area in degrees-squared and antenna efficiency
            self.G_tx = 46.15 - dB(A_theta) + dB(eta_tx)
        
        # EIRP - Effective Isotropic Radiated Power = Forward power + Antenna gain
        self.EIRP = self.G_tx + self.P