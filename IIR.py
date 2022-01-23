import numpy as np

class IIR:
    """Essa classe implementa as funções de um filtro de segunda ordem IIR"""
    def __init__(self):
        """Inicialize filter"""
        self.a0 = 0.0
        self.a1 = 0.0
        self.a2 = 0.0
        self.b0 = 0.0
        self.b1 = 0.0
        self.b2 = 0.0
        self.u0 = 0.0
        self.u1 = 0.0
        self.u2 = 0.0
        self.y0 = 0.0
        self.y1 = 0.0
        self.y2 = 0.0
    
    def reset(self):
        """reset filter"""
        self.u0 = 0.0
        self.u1 = 0.0
        self.u2 = 0.0
        self.y0 = 0.0
        self.y1 = 0.0
        self.y2 = 0.0
    
    def coff_update(self,a0,a1,a2,b1,b2):
        """Update filter coefficients"""
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2
        
    def bypass_filter(self):
        """Coeff for by pass filter config: y = u"""
        self.a0 = 1.0
        self.a1 = 0.0
        self.a2 = 0.0
        self.b0 = 1.0
        self.b1 = 0.0
        self.b2 = 0.0

    def run_filter(self,u0):
        """Compute filter input u0 and return filter output y0"""
        self.u2 = self.u1
        self.u1 = self.u0
        self.u0 = u0        
        self.y2 = self.y1
        self.y1 = self.y0
        self.y0 = (self.a0 * self.u0 +
                   self.a1 * self.u1 +
                   self.a2 * self.u2 -
                   self.b1 * self.y1 -
                   self.b2 * self.y2 )
        return self.y0

filtro = IIR()
