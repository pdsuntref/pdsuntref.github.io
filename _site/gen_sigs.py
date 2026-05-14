import numpy as np
import soundfile as sf

# -----------------------
# Parámetros generales
# -----------------------
fs = 44100          # Hz
duration = 1.0      # segundos
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# -----------------------
# Función: normalización
# -----------------------
def normalize(signal):
    return signal / np.max(np.abs(signal))

# -----------------------
# 1) Suma de tonos puros
# -----------------------
freqs = [440, 880, 1760]  # A4, A5, A6

pure_tones = sum(np.sin(2 * np.pi * f * t) for f in freqs)
pure_tones = normalize(pure_tones)

# Ruido blanco en distintas amplitudes
noise_levels = [0.01, 0.05, 0.2]

for amp in noise_levels:
    noise = amp * np.random.randn(len(t))
    signal = normalize(pure_tones + noise)

    filename = f"tonos_ruido_{amp:.2f}.wav"
    sf.write(filename, signal, fs)

# -----------------------
# 2) Señal "musical"
# -----------------------
# Una pequeña melodía sintética
notes = [261.63, 293.66, 329.63, 349.23, 392.00]  # Do Re Mi Fa Sol
note_duration = duration / len(notes)

music = np.zeros_like(t)

for i, f in enumerate(notes):
    start = int(i * note_duration * fs)
    end = int((i + 1) * note_duration * fs)

    tt = t[start:end]
    music[start:end] = np.sin(2 * np.pi * f * tt)

music = normalize(music)

for amp in noise_levels:
    noise = amp * np.random.randn(len(t))
    signal = normalize(music + noise)

    filename = f"musica_ruido_{amp:.2f}.wav"
    sf.write(filename, signal, fs)

print("Archivos generados correctamente.")
