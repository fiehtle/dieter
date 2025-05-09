# Import dependencies
import sys
import os
# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(project_root)

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from python.src.vco import VCO

class WaveformPlayer:
    def __init__(self):
        self.vco = VCO()
        self.frequency = 440 # A4 note
        self.duration = 1.0 # 1 second
        self.stream = None

    def play_waveform(self, waveform_type):
        """Generate and play the selected waveform"""
        if waveform_type == "sine":
            wave = self.vco.generate_sine(self.frequency, self.duration)
        elif waveform_type == "square":
            wave = self.vco.generate_square(self.frequency, self.duration)
        elif waveform_type == "triangle":
            wave = self.vco.generate_triangle(self.frequency, self.duration)
        elif waveform_type == "sawtooth":
            wave = self.vco.generate_sawtooth(self.frequency, self.duration)
            
        # Stop any currently playing sound
        if self.stream is not None:
            self.stream.stop()
            
        # Play the new waveform
        self.stream = sd.play(wave, self.vco.sample_rate)
        
        # Update the visualization
        # Only show first 1000 samples (about 23ms)
        samples_to_show = 1000
        t = np.linspace(0, samples_to_show / self.vco.sample_rate * 1000, samples_to_show)  # time in ms
        line.set_data(t, wave[:samples_to_show])
        ax.set_xlim(0, t[-1])
        fig.canvas.draw_idle()

    def stop_playing(self):
        """Stop the currently playing waveform"""
        if self.stream is not None:
            self.stream.stop()
            self.stream = None
            
# Create the player
player = WaveformPlayer()

# Create the figure and buttons
fig, ax = plt.subplots(figsize=(10, 6))

# Set up the waveform display
ax.set_ylim(-1.2, 1.2)
ax.set_title('Waveform Visualization')
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Amplitude')
ax.grid(True)
line, = ax.plot([], [], lw=2)

# Create the buttons - Adjust positions to accommodate 4 waveform buttons
button_ax = plt.axes([0.1, 0.05, 0.15, 0.075])
sine_button = plt.Button(button_ax, "Sine Wave")

button_ax = plt.axes([0.3, 0.05, 0.15, 0.075])
square_button = plt.Button(button_ax, "Square Wave")

button_ax = plt.axes([0.5, 0.05, 0.15, 0.075])
triangle_button = plt.Button(button_ax, "Triangle Wave")

button_ax = plt.axes([0.7, 0.05, 0.15, 0.075])
sawtooth_button = plt.Button(button_ax, "Sawtooth Wave")

# Create the stop button
stop_ax = plt.axes([0.4, 0.15, 0.2, 0.075])
stop_button = plt.Button(stop_ax, "Stop")

# Add a frequency slider (FIXED position to avoid overlap)
freq_ax = plt.axes([0.1, 0.25, 0.8, 0.05])
freq_slider = plt.Slider(
    ax=freq_ax,
    label='Frequency (Hz)',
    valmin=20,
    valmax=2000,
    valinit=440,
)

# Button event handlers
def on_sine_click(event):
    player.play_waveform("sine")

def on_square_click(event):
    player.play_waveform("square")

def on_triangle_click(event):
    player.play_waveform("triangle")

def on_sawtooth_click(event):
    player.play_waveform("sawtooth")

# Handle frequency slider changes
def on_freq_change(val):
    player.frequency = val

# Connect the buttons to the event handlers
sine_button.on_clicked(on_sine_click)
square_button.on_clicked(on_square_click)
triangle_button.on_clicked(on_triangle_click)
sawtooth_button.on_clicked(on_sawtooth_click)
stop_button.on_clicked(lambda event: player.stop_playing())

# Connect slider
freq_slider.on_changed(on_freq_change)

plt.show()