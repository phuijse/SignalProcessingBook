# Para visualizar gráficos en la terminal interactiva
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'ipympl')


"""
# Actividad en clases: Diseño de filtros FIR

Objetivos: 

- Aprender a utilizar scipy.signal.firwin para diseñar filtros FIR
- Filtrar señales de audio con filtros FIR

 
"""

import numpy as np
import scipy.fft
import scipy.signal
import matplotlib.pylab as plt
from IPython.display import display
import librosa
from utils import Audio

def listen_signal(signal: np.ndarray, Fs: int=44100, normalize:bool=True) -> None:
    if normalize:
        signal = signal.copy()/np.amax(np.absolute(signal))
    display(Audio(signal, rate=Fs))

"""

Sea la siguiente señal:

"""

data, Fs = librosa.load("nomekop.ogg", sr=8000)

Nw = 512
freq, ttime, Sxx = scipy.signal.spectrogram(data, fs=Fs, window='hamming', nperseg=Nw, noverlap=Nw//1.5)

fig, ax = plt.subplots(1, figsize=(8, 3), tight_layout=True)
ax.pcolormesh(ttime, freq, np.log10(Sxx+1e-5), shading='auto', cmap=plt.cm.magma); 
ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Frecuencia [Hz]')  
listen_signal(data, Fs=Fs)


"""

El siguiente código de ejemplo busca atenuar el primer personaje preservando lo más posible del segundo personaje

- Estudien atentamente la rutina y el resultado 
- ¿Puedes mejorar el resultado modificando las frecuencias de corte?

"""

h = scipy.signal.firwin(numtaps=1000+1, cutoff=[50, 700, 1900, 2100], pass_zero=False, window='hamming', fs=Fs)
freq_response, response = scipy.signal.freqz(h, fs=Fs)
data_filt = scipy.signal.convolve(data, h)
freq, ttime, Sxx = scipy.signal.spectrogram(data_filt, fs=Fs, window='hamming', nperseg=Nw, noverlap=Nw//1.5)

# Resultados:
fig, ax = plt.subplots(1, 2, figsize=(7, 2), tight_layout=True)
ax[0].plot(h); 
ax[1].semilogy(freq_response, np.abs(response))
fig, ax = plt.subplots(1, figsize=(8, 3), tight_layout=True)
ax.pcolormesh(ttime, freq, np.log10(Sxx+1e-5), shading='auto', cmap=plt.cm.magma); 
ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Frecuencia [Hz]')  
listen_signal(data_filt, Fs=Fs)

"""

- Modifique L y el tipo de ventana (truncamiento). Discuta sobre como cambia el resultado en términos visuales y acústicos
- Diseñe y pruebe un filtro FIR que atenue al segundo personaje y preserve al primer personaje

"""





