import matplotlib.pyplot as plt
import numpy as np

from IIR import IIR

Filtro = IIR()
Filtro.coff_update( 0.07977956016104085,
                    0.2925700438921773,
                    0.4207721339385776,
                    0.2925700438921773,
                    -0.07977956016104085)

u = np.ones(533,dtype=np.float32)
y = np.zeros(533,dtype=np.float32)
t = np.linspace(0,533,533)

for i in range(533):
    y[i] = Filtro.run_filter(u[i])

plt.plot(t,y)
plt.show()

