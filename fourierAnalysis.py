import numpy as np
import matplotlib.pyplot as plt

# Define parameters
fs = 8000  # Sampling frequency (8 kHz)
T = 0.01   # Duration (10 ms)
f1 = 440   # Frequency of first tone (A4)
f2 = 880   # Frequency of second tone (A5)
f3 = 1320  # Frequency of third tone (E6)

# Create time vector
t = np.linspace(0, T, int(fs*T), endpoint=False)  # 80 samples

# Generate the signal (sum of 3 sine waves)
x = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) + np.sin(2 * np.pi * f3 * t)

# Compute the Fourier Transform
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(X), 1/fs)

# Get the magnitude spectrum
magnitude = np.abs(X)

# Plot the signal and its Fourier transform
plt.figure(figsize=(14, 6))

# Plot the original signal
plt.subplot(1, 2, 1)
plt.plot(t, x)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the magnitude spectrum
plt.subplot(1, 2, 2)
plt.plot(frequencies[:len(frequencies)//2], magnitude[:len(magnitude)//2])  # Only positive frequencies
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
