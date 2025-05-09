# Import dependencies
import sys
import os
# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(project_root)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import sounddevice as sd
from python.src.vco import VCO
from python.src.vcf import VCF

class FilterDemo:
    def __init__(self):
        self.vco = VCO()
        self.vcf = VCF()
        self.frequency = 220  # A3 note
        self.cutoff = 1000    # Initial cutoff at 1000Hz
        self.resonance = 0.3  # Medium resonance
        self.duration = 2.0   # 2 second buffer
        self.stream = None
        self.waveform_type = "sawtooth"  # Default to sawtooth (most harmonics)
        
        # Generate initial audio and apply filter
        self.update_audio()
        
    def update_audio(self):
        """Generate waveform and apply filter with current settings"""
        # Generate raw waveform
        if self.waveform_type == "sine":
            self.raw_wave = self.vco.generate_sine(self.frequency, self.duration)
        elif self.waveform_type == "square":
            self.raw_wave = self.vco.generate_square(self.frequency, self.duration)
        elif self.waveform_type == "triangle":
            self.raw_wave = self.vco.generate_triangle(self.frequency, self.duration)
        else:  # sawtooth
            self.raw_wave = self.vco.generate_sawtooth(self.frequency, self.duration)
            
        # Apply filter to the raw wave
        self.filtered_wave = self.vcf.apply_filter(
            self.raw_wave, 
            self.cutoff, 
            self.resonance
        )
        
        # Update plots
        self.update_plots()
    
    def update_plots(self):
        """Update the waveform display with current signals"""
        # Clear current plots
        ax_time.clear()
        ax_filtered.clear()
        
        # Set up time plots with first 1000 samples (about 23ms)
        samples_to_show = 1000
        t = np.linspace(0, samples_to_show / self.vco.sample_rate * 1000, samples_to_show)
        
        # Plot raw waveform
        ax_time.plot(t, self.raw_wave[:samples_to_show], label='Raw')
        ax_time.set_ylabel('Amplitude')
        ax_time.set_title('Raw Waveform')
        ax_time.set_ylim(-1.2, 1.2)
        ax_time.grid(True)
        
        # Plot filtered waveform
        ax_filtered.plot(t, self.filtered_wave[:samples_to_show], label='Filtered', color='orange')
        ax_filtered.set_xlabel('Time (ms)')
        ax_filtered.set_ylabel('Amplitude')
        ax_filtered.set_title(f'Filtered Waveform (Cutoff: {self.cutoff}Hz, Res: {self.resonance:.1f})')
        ax_filtered.set_ylim(-1.2, 1.2)
        ax_filtered.grid(True)
        
        fig.canvas.draw_idle()
    
    def play_audio(self, filtered=True):
        """Play either the raw or filtered audio"""
        # Stop any currently playing sound
        if self.stream is not None:
            self.stream.stop()
            
        # Choose which audio to play
        audio = self.filtered_wave if filtered else self.raw_wave
        
        # Play the audio
        self.stream = sd.play(audio, self.vco.sample_rate)
    
    def stop_audio(self):
        """Stop any playing audio"""
        if self.stream is not None:
            self.stream.stop()
            self.stream = None

# Create the demo
demo = FilterDemo()

# Create the figure and subplots for visualization
fig, (ax_time, ax_filtered) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(bottom=0.3)  # Make room for sliders

# Add sliders
# Cutoff frequency slider
cutoff_ax = plt.axes([0.15, 0.20, 0.7, 0.03])
cutoff_slider = Slider(
    ax=cutoff_ax,
    label='Cutoff Freq (Hz)',
    valmin=50,
    valmax=5000,
    valinit=demo.cutoff,
    valstep=10
)

# Resonance slider
res_ax = plt.axes([0.15, 0.15, 0.7, 0.03])
res_slider = Slider(
    ax=res_ax,
    label='Resonance',
    valmin=0.0,
    valmax=0.9,
    valinit=demo.resonance,
    valstep=0.05
)

# Oscillator frequency slider
freq_ax = plt.axes([0.15, 0.25, 0.7, 0.03])
freq_slider = Slider(
    ax=freq_ax,
    label='Frequency (Hz)',
    valmin=50,
    valmax=500,
    valinit=demo.frequency,
    valstep=1
)

# Add buttons for playing sounds and changing waveform
# Play buttons
play_raw_ax = plt.axes([0.15, 0.05, 0.2, 0.05])
play_raw_button = Button(play_raw_ax, "Play Raw")

play_filt_ax = plt.axes([0.4, 0.05, 0.2, 0.05])
play_filt_button = Button(play_filt_ax, "Play Filtered")

stop_ax = plt.axes([0.65, 0.05, 0.2, 0.05])
stop_button = Button(stop_ax, "Stop")

# Waveform selection
wave_sine_ax = plt.axes([0.1, 0.01, 0.15, 0.03])
wave_square_ax = plt.axes([0.3, 0.01, 0.15, 0.03])
wave_tri_ax = plt.axes([0.5, 0.01, 0.15, 0.03])
wave_saw_ax = plt.axes([0.7, 0.01, 0.15, 0.03])

wave_sine_button = Button(wave_sine_ax, "Sine")
wave_square_button = Button(wave_square_ax, "Square")
wave_tri_button = Button(wave_tri_ax, "Triangle")
wave_saw_button = Button(wave_saw_ax, "Sawtooth")

# Update functions
def update_cutoff(val):
    demo.cutoff = val
    demo.update_audio()
    
def update_resonance(val):
    demo.resonance = val
    demo.update_audio()

def update_frequency(val):
    demo.frequency = val
    demo.update_audio()
    
def on_play_raw(event):
    demo.play_audio(filtered=False)
    
def on_play_filtered(event):
    demo.play_audio(filtered=True)
    
def on_stop(event):
    demo.stop_audio()
    
def on_wave_sine(event):
    demo.waveform_type = "sine"
    demo.update_audio()
    
def on_wave_square(event):
    demo.waveform_type = "square"
    demo.update_audio()
    
def on_wave_tri(event):
    demo.waveform_type = "triangle"
    demo.update_audio()
    
def on_wave_saw(event):
    demo.waveform_type = "sawtooth"
    demo.update_audio()

# Connect the callbacks
cutoff_slider.on_changed(update_cutoff)
res_slider.on_changed(update_resonance)
freq_slider.on_changed(update_frequency)

play_raw_button.on_clicked(on_play_raw)
play_filt_button.on_clicked(on_play_filtered)
stop_button.on_clicked(on_stop)

wave_sine_button.on_clicked(on_wave_sine)
wave_square_button.on_clicked(on_wave_square)
wave_tri_button.on_clicked(on_wave_tri)
wave_saw_button.on_clicked(on_wave_saw)

# Initial update
demo.update_plots()

plt.show() 