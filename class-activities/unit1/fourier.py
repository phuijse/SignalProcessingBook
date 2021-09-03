# Para visualizar gráficos en la terminal interactiva
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'ipympl')

"""

# Actividad en clases: FFT con scipy
 
Objetivos:

- Aprender a utilizar las funciones de `scipy.fft`
- Visualizar el espectro de distintas señales
- Ver como el ruido afecta el espectro

"""

import numpy as np
import scipy.fft
import scipy.signal
import matplotlib.pyplot as plt

Fs = 50
t = np.arange(0, 10, step=1/Fs)
s = np.cos(2.0*np.pi*t*1.2)

S = scipy.fft.rfft(s)
f = scipy.fft.rfftfreq(n=len(t), d=1/Fs)

fig, ax = plt.subplots(figsize=(5, 3), tight_layout=True)
ax.plot(f, np.absolute(S))
ax.set_xlabel('Frecuencia [Hz]')



"""

I) Obtenga y visualice el espectro de magnitud para cada una de las siguientes señales. Discuta con sus compañeros acerca de las diferencias que observa entre los espectros. 
1. Una suma de dos sinusoides de distinta frecuencia fundamental
2. Una señal periódica triangular, se recomienda usar scipy.signal.sawtooth

II) Considere ahora sólo la señal suma de dos sinusoides. Súmele un vector de ruido blanco gaussiano usando 

s += np.random.randn(len(t))*sigma

donde sigma es la desviación estándar del ruido. Considere los casos sigma=0.5, 1 y 2

Visualice el espectro para cada caso y discuta con sus compañeros respecto al efecto del ruido blanco en el espectro. 

"""






