import numpy as np
from .utils import dB, lin, pi, c


class Antenna:
    '''
    The general Antenna class
    
    Input Parameters
    ----------------
    D           Antenna diameter        m
    eta         Antenna efficiency      -
    '''
    
    def __init__(self, D=None, eta=0.5, platform=None):
        self.D = D
        self.eta = eta
        self.platform = platform
        
        # Will change based on running mode in Link object
        self.is_tx = False


    def set_operating_params(self, line_loss, frequency, power=None):
        ''' Link object assigns operating parameters '''

        self.P = power
        self.f = frequency
        self.L_line = line_loss
        
        if power is not None:   self.is_tx = True


    def calculate(self):
        ''' Calculate link parameters for the antenna '''

        # TX Antenna half-power beamwidth in degrees
        # Augumented for f in Hz, D in m
        self.beamwidth = 21e9 / (self.f * self.D)

        # Antenna gain in dB 
        # Specific to antennas with a circularly symmetric radiating aperture
        self.G = 2*dB(pi/c) + 2*dB(self.D) + 2*dB(self.f) + dB(self.eta)
        
        # EIRP - Effective Isotropic Radiated Power = Forward power + Antenna gain
        if self.is_tx:  self.EIRP = self.G + dB(self.P) - self.L_line



class ShapedAntenna(Antenna):
    '''
    Extends the general Antenna class to account for beam shaping
    
    Input Parameters
    ----------------
    eta         Antenna efficiency      -
    A_theta     Coverage area           degrees-squared
    '''
    
    def __init__(self, A_theta=13.3, eta=0.7, platform=None):
        super().__init__(self, eta=eta, platform=platform)
        
        # Coverage area is measured in degrees-squared
        self.A_theta = A_theta


    # Override the calculate() method
    def calculate(self):
        ''' Gain for shaped antennas - directivity is a function of coverage area in degrees-squared, not frequency! '''

        # Beam shaping - directivity is a function of coverage area in degrees-squared and antenna efficiency
        self.G = 46.15 - dB(self.A_theta) + dB(self.eta)

        # EIRP - Effective Isotropic Radiated Power = Forward power + Antenna gain
        if self.is_tx:  self.EIRP = self.G + dB(self.P) - self.L_line



class PhasedArray(Antenna):
    '''
    Defines a phased array of antennas
    '''
    
    None