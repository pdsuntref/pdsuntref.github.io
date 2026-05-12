import numpy as np
from scipy.signal import firwin

fs = 44100
fc = 1000
transition = 100

# Orden estimado para ventana Hamming
N = int(np.ceil(3.3 * fs / transition))
if N % 2 == 0:
    N += 1

# Diseño FIR
h = firwin(
    numtaps=N,
    cutoff=fc,
    window='hamming',
    fs=fs,
    pass_zero='lowpass'
)

# Guardar como archivo numpy
np.save("fir_hamming_1000Hz.npy", h)

print("Coeficientes guardados en fir_hamming_1000Hz.npy")
print("Cantidad de coeficientes:", len(h))
