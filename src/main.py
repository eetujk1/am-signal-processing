import numpy as np
import matplotlib.pyplot as plt


frequency = 1000
sampling_rate = 1000000
duration = 0.01
modulation_index = 0.5

t = np.arange(0, duration, 1/sampling_rate)

message = np.sin(2*np.pi*frequency*t)

carrier_frequency = 10000

carrier = np.sin(2*np.pi*carrier_frequency*t)

am_signal = (1+modulation_index*message)*carrier

plt.figure(figsize=(10, 8))


#Plot the message-wave
plt.subplot(3, 1, 1)
plt.plot(t, message)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Message")

#Plot carrier-wave
plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Carrier")




plt.subplot(3, 1, 3)
plt.plot(t, am_signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("AM-signal")
plt.grid()
plt.savefig("results/am_signals.png")
plt.show()

frequencies = np.fft.fftfreq(len(am_signal), 1/sampling_rate)
fft = np.fft.fft(am_signal)
magnitude = np.abs(fft)/len(am_signal)

plt.xlim(0, 20000)
plt.plot(frequencies, magnitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("AM Signal spectrum")
plt.grid()
plt.savefig("results/am_signals_fft.png")
plt.show()


snr_db = 10

signal_power = np.mean(am_signal**2)
noise_power = signal_power / (10**(snr_db/10))

noise_std = np.sqrt(noise_power)

noise = np.random.normal(
    0,
    noise_std,
    len(am_signal)
)

noisy_signal = am_signal + noise

plt.figure(figsize=(10, 5))

plt.plot(t, noisy_signal, alpha=0.5, label="AM signal + noise")
plt.plot(t, am_signal, linewidth=2.5, label="AM signal")

plt.xlim(0, 0.001)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("AM Signal with Noise")
plt.legend()
plt.grid()
plt.savefig("results/am_signals_noise.png")
plt.show()