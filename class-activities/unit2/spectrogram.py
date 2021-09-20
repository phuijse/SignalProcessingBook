# Para visualizar gráficos en la terminal interactiva
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'ipympl')


"""
# Actividad en clases: Análisis de señales no estacionarias con espectrogramas

Objetivos: 

- Obtener espectrogramas usando Python
- Estudiar la influencia del tamaño de la ventana en la estimación
- Analizar espectrogramas en señales de audio sintéticas y reales

 
"""

import numpy as np
import scipy.fft
import scipy.signal
import matplotlib.pylab as plt
from IPython.display import display
import librosa
from utils import Audio

def listen_signal(signal: np.ndarray, Fs: int=44100) -> None:
    display(Audio(signal, rate=Fs))

"""

Referencia: https://phuijse.github.io/UACH-INFO183/lectures/unit2/lecture1.html#chirrido-o-chirp

Utilice la función scipy.signal.spectrogram para estimar el espectrograma de la señal chirp. Considere las siguientes combinaciones de parámetros

- Para el largo de la ventana (nperseg) pruebe los valores 128, 512 y 2048
- Para la función de ventana (window) utilice la ventana de rectangular ('boxcar') y la ventana de Hamming ('hamming')

Compare y discuta sobre lo que observa
"""

f0, f1, Fs = 4000, 2000, 44100
t = np.arange(0, 0.5, step=1./Fs); 
s = 0.1*scipy.signal.chirp(t, f0=f0, f1=f1, t1=t[-1], method='quadratic')
listen_signal(s, Fs=Fs)



"""
Referencia: https://phuijse.github.io/UACH-INFO183/lectures/unit2/lecture1.html#espectrograma-de-una-senal-de-voz

Realice un procedimiento similar al anterior pero para una señal musical. Se recomienda visualizar el logaritmo del espectrograma (ver referencia)

Grafique la señal junto al espectrograma que usted considere cualitativamente mejor. Discutan sobre lo que observan intentando relacionar lo que escuchan en la señal con lo que visualizan en el espectrograma

"""
import librosa
data, Fs = librosa.load("DPSAU.ogg", sr=8000)
listen_signal(data, Fs=Fs)





