import numpy as np

class VCO:
    """
    Voltage Controlled Oscillator (VCO)
    Generates various waveforms at specified frequencies
    """
    def __init__(self, sample_rate=44100):
        """ 
        Initialize the VCO
        Args:
            sample_rate: Number of samples per second (default: 44100Hz - CD quality)
        """
        self.sample_rate = sample_rate

    def generate_sine(self, frequency, duration):
        """
        Generate a sine wave
        Args:
            frequency: Frequency of the sine wave in Hz (e.g. 440Hz for A4)
            duration: Length of the waveform in seconds
        Returns:
            numpy array of samples
        """
        
        # Create time array from 0 to duration
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)

        # Generate sine wave
        wave = np.sin(2 * np.pi * frequency * t)

        return wave

    def generate_square(self, frequency, duration):
        """
        Generate a square wave
        Args:
            frequency: Frequency of the square wave in Hz (e.g. 440Hz for A4)
            duration: Length of the waveform in seconds
        Returns:    
            numpy array of samples
        """

        # Create time array from 0 to duration
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)

        # Generate square wave
        wave = np.sign(np.sin(2 * np.pi * frequency * t))

        return wave

    def generate_triangle(self, frequency, duration):
        """
        Generate a triangle wave
        Args:
            frequency: Frequency of the triangle wave in Hz (e.g. 440Hz for A4)
            duration: Length of the waveform in seconds
        Returns:
            numpy array of samples  
        """

        # Create time array from 0 to duration
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)

        # Generate triangle wave using a more accurate formula
        # This creates a proper triangle wave with peaks at +1 and -1
        wave = 2 * np.abs(2 * (t * frequency - np.floor(t * frequency + 0.5))) - 1

        return wave
    
    def generate_sawtooth(self, frequency, duration):
        """
        Generate a sawtooth wave
        Args:
            frequency: Frequency of the sawtooth wave in Hz (e.g. 440Hz for A4)
            duration: Length of the waveform in seconds
        Returns:
            numpy array of samples
        """
        
        # Create time array from 0 to duration
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        
        # Generate sawtooth wave
        # This formula produces a sawtooth that rises from -1 to 1
        wave = 2 * (t * frequency - np.floor(t * frequency + 0.5))
        
        return wave
    
    
    
    
    
    