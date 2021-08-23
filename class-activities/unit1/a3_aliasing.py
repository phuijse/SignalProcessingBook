"""
# Actividad en clases: Aliasing
 
- Consideremos la siguiente señal periódica con componentes 1Hz, 12Hz y 23Hz, respectivamente

$$
s(t) = \cos(2\pi t) + 0.5 \cos(2\pi 12 t) + 0.25 \cos(2\pi 23 t)
$$

"""
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'ipympl')
import numpy as np
import matplotlib.pyplot as plt

Fs = 100
t = np.arange(0, 5, step=1/Fs)
s = lambda t: np.cos(2.0*np.pi*t) + 0.5*np.cos(2.0*np.pi*t*12) + 0.25*np.cos(2.0*np.pi*t*23)

fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(t, s(t))

"""
## Parte 1 

Escribamos una función que calcule y gráfique el espectro de amplitud y fase. Estudiemos y entendamos sus componentes

"""



"""
## Parte 2

Remuestremos la señal disminuyendo su frecuecia de muestreo y observemos el espectro resultante. Identifiquemos los "aliases" en el nuevo espectro
"""



"""
## Parte 3

Use el resultado del teorema del muestreo para reconstruir la señal original en cada caso y visualice el resultado. ¿En qué casos es posible una reconstrucción perfecta?

$$
s(t) = \sum_{n=-\infty}^{\infty} s[n] \text{sinc}(\pi F_s (t - n /F_s) )
$$

"""




