# Para visualizar gráficos en la terminal interactiva
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'ipympl')


"""
# Actividad en clases: Aliasing
 
Consideremos la siguiente señal periódica con componentes 1Hz, 12Hz y 23Hz, respectivamente

"""

import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

create_time = lambda Fs: np.arange(0, 5, step=1/Fs)
create_signal = lambda t: np.cos(2.0*np.pi*t) + 0.5*np.cos(2.0*np.pi*t*12) + 0.25*np.cos(2.0*np.pi*t*23)

Fs = 100
t = create_time(Fs)
s = create_signal(t)
S = scipy.fft.rfft(s)
f = scipy.fft.rfftfreq(n=len(t), d=1/Fs)

fig, ax = plt.subplots(2, 1, figsize=(5, 3))
ax[0].plot(t, s)
ax[1].plot(f, np.abs(S))


"""
## Parte 1

Remuestree la señal disminuyendo su frecuencia de muestreo a la mitad y observe el espectro resultante. Identifique los "aliases" en el nuevo espectro
"""



"""
## Parte 2

Use el resultado del teorema del muestreo para reconstruir la señal original en cada caso y visualice el resultado. ¿En qué casos es posible una reconstrucción perfecta?

$$
s(t) = \sum_{n=-\infty}^{\infty} s[n] \text{sinc}(\pi F_s (t - n /F_s) )
$$

"""




