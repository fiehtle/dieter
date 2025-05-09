# A simple script to test the setup and show some basic waveform generation
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Generate a simple sine wave
sample_rate = 44100 # standard audio sample rate
duration = 0.1      # 100ms
t = np.linspace(0, duration, int(sample_rate * duration), False) 
freq = 440         # 440 Hz middle A
sine_wave = np.sin(2 * np.pi * freq * t)

# Plot the first few milliseconds
plt.plot(t[:1000], sine_wave[:1000])
plt.title('440 Hz Sine Wave (first few ms)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# Play the sine wave
sd.play(sine_wave, sample_rate)
sd.wait() # wait until the sound is finished playing



