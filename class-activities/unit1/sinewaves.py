    # Para visualizar gráficos en la terminal interactiva
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'ipympl')

"""

# Actividad en clases: Series de Fourier
 
Objetivos:
- Componer señales periodicas en base a sinusoides
- Visualizar señales con matplotlib
- Escuchar las señales con IPython
- Bonus: Explorar algunos efectos sonoros 

"""

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from utils import Audio
from typing import Tuple

def create_tone(freq: float=220., Fs: int=44100, volume:float=0.8) -> Tuple[np.ndarray, np.ndarray]:
    time = np.arange(0, 2, step=1/Fs)
    waveform = np.cos(2.0*np.pi*freq*time)
    return time, volume*waveform/np.amax(np.absolute(waveform))

def plot_and_listen(time: np.ndarray, signal: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize=(6, 3), tight_layout=True)
    ax.plot(time, signal)
    ax.set_xlim([0, 0.05])
    ax.set_ylim([-1, 1])
    ax.set_ylabel('Amplitud')
    ax.set_xlabel('Segundos')
    display(Audio(signal, rate=int(1/(time[1] - time[0]))))

time, signal = create_tone(freq=440)
plot_and_listen(time, signal)

"""
Genere tonos puros con distinta frecuencia, visualice y escuche las señales

Implemente una función que genere una señal triangular en base a su serie de Fourier. La función debe recibir como argumentos
- la frecuencia fundamental
- la frecuencia de muestreo
- el volumen
- el número de armónicos

Visualize y escuche la señal generada. Discuta con sus compañeros sobre los efectos de modificar los distintos parámetros
"""