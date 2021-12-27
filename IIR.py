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
    
    def coff_update(self,a0,a1,a2,b0,b1,b2):
        """Update filter coefficients"""
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2

filtro = IIR()
print(filtro.a0)
filtro.coff_update(1,1,1,1,1,1)
print(filtro.a0)
