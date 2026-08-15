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