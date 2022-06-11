import numpy as np

### Utility functions - will move somewhere better ###
dB = lambda x: 10 * np.log10(x)         # Decibel conversion lambda
lin = lambda x: 10 ** (x / 10)          # Linear conversion lambda
pi = np.pi                              # Good old pi
c = 299792458                           # Speed of light


class Antenna:
    '''
    The general Antenna class
    
    Contains the following models:
    - Platform()
    
    Input Parameters
    ----------------
    D           Antenna diameter        m
    P           Transmit power          W
    eta         Antenna efficiency      -
    '''
    
    def __init__(self, D=None, P=0, eta=0.5, L_line=4, platform=None):
        self.D = D
        self.P = P
        self.eta = eta
        self.L_line = L_line
        self.platform = platform
        
        self.beamwidth = 0
    
    
    def set_beamwidth(self, frequency):
        '''
        TX Antenna half-power beamwidth - in degrees
        Augumented for f in Hz, D in m
        '''
        
        self.beamwidth = 21e9 / (frequency * self.D)


    def set_power(self, power):
        '''Set the transmit power in W'''
        self.P = power


    def set_gain(self, frequency):
        '''Antenna gain in dB - specific to antennas with a circularly symmetric radiating aperture'''

        # Augumented for f in Hz, D in m
        self.G = 2*dB(pi/c) + 2*dB(self.D) + 2*dB(frequency) + dB(self.eta)

        # EIRP - Effective Isotropic Radiated Power = Forward power + Antenna gain
        self.EIRP = self.G + dB(self.P) - self.L_line



class ShapedAntenna(Antenna):
    '''
    Extends the general Antenna class to account for beam shaping
    
    Input Parameters
    ----------------
    D           Antenna diameter        m
    P           Transmit power          W
    eta         Antenna efficiency      -
    A_theta     Coverage area           degrees-squared
    '''
    
    def __init__(self, P=0, eta=0.7, L_line=-2, A_theta=13.3, platform=None):
        super().__init__(self, P, eta, L_line, platform)
        
        # Coverage area is measured in degrees-squared
        self.A_theta = A_theta


    # Override the set_gain method
    def set_gain(self, frequency):
        '''
        Gain for shaped antennas - directivity is a function of coverage area in degrees-squared and antenna efficiency
        '''

        # Beam shaping - directivity is a function of coverage area in degrees-squared and antenna efficiency
        self.G = 46.15 - dB(self.A_theta) + dB(self.eta)

        # EIRP - Effective Isotropic Radiated Power = Forward power + Antenna gain
        self.EIRP = self.G + self.P