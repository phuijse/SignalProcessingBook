# Para visualizar gráficos en la terminal interactiva
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'ipympl')


"""
# Actividad en clases: Aliasing

Objetivos: 

- Reconstruir señales usando los resultados del teorema del muestreo
- Estudiar de forma práctica el fenomeno de aliasing

 
Para esta actividad consideremos la siguiente señal periódica con componentes 1Hz, 12Hz y 23Hz, respectivamente

"""

import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

Fs = 1000
tn = np.arange(0, 2, step=1/Fs)
sn = np.cos(2.0*np.pi*tn) + 0.5*np.cos(2.0*np.pi*tn*12) + 0.25*np.cos(2.0*np.pi*tn*23)
S = scipy.fft.rfft(sn)
f = scipy.fft.rfftfreq(n=len(tn), d=1/Fs)

fig, ax = plt.subplots(2, 1, figsize=(5, 3), tight_layout=True)
ax[0].plot(tn, sn, '.', markersize=1)
ax[1].plot(f, np.abs(S))

"""

Primero visualice la señal y el espectro de amplitud para Fs=1000, Fs=50, Fs=10. ¿En qué casos se pueden detectar sin ambiguedad las frecuencias de la señal? 

"""


"""
El teorema del muestreo dice que una señal digital sn cuya frecuencia máxima sea menor que la mitad de la frecuencia de muestreo Fs puede reconstruirse sin perdidas usando la fórmula de interpolación indicada en https://phuijse.github.io/UACH-INFO183/lectures/unit1/lecture4.html#teorema-del-muestreo

que usando NumPy sería

s = np.sum(sn*np.sinc(Fs*(t-tn)))

Utilice la formula para reconstruir la señal usando una frecuencia de muestreo arbitrariamente alta (Fs = 10000) y discuta sobre lo que observa

"""

