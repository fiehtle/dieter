import numpy as np

class VCF:
    """
    Voltage Controlled Filter (VCF)
    Shapes sound by removing or amplifying frequencies
    """

    def __init__(self, sample_rate=44100):
        """
        Initialize the VCF
        Args:
            sample_rate: Number of samples per second
        """
        self.sample_rate = sample_rate
        # Filter memory - needed to remember previous samples
        self.prev_input = 0
        self.prev_output = 0
    
    def apply_filter(self, input_signal, cutoff_freq, resonance = 0.5, filter_type = "low_pass"):
        """ 
        Apply a filter to the input signal
        Args:
            input_signal: Array of audio samples to filter 
            cutoff_freq: Cutoff frequency in Hz (20-20000)
            resonance: Resonance (0.0-1.0)
            filter_type: Type of filter to apply ("low_pass", "high_pass", "band_pass") 
        Returns:
            Filtered signal as numpy array
        """
        # Safety: ensure values are in valid ranges
        cutoff_freq = np.clip(cutoff_freq, 20, self.sample_rate/2)
        resonance = np.clip(resonance, 0.0, 0.99)

        # Select filter type
        if filter_type == "low_pass":
            return self._apply_low_pass(input_signal, cutoff_freq, resonance)
        elif filter_type == "high_pass":
            # Placeholder - currently returns unfiltered signal
            # We'll implement high-pass later
            print("High-pass filter not implemented yet")
            return input_signal
        elif filter_type == "band_pass":
            # Placeholder - currently returns unfiltered signal
            # We'll implement band-pass later
            print("Band-pass filter not implemented yet")
            return input_signal
        else:
            # Default to low-pass if unknown filter type
            return self._apply_low_pass(input_signal, cutoff_freq, resonance)

def _apply_low_pass(self, input_signal, cutoff_freq, resonance):
    """
    Apply a low-pass filter to the input signal
    Uses a simple first-order IIR filter with resonance
    """
    # Calculate filter coefficients (controls how much past sound to keep)
    # Lower cutoff = more past sound (smoother)
    alpha = np.exp(-2 * np.pi * cutoff_freq / self.sample_rate)
    # Adjust based on resonance
    alpha = alpha * (1 - 0.5 * resonance)

    # Create output array
    output = np.zeros_like(input_signal)

    # Reset filter state for consistent results
    self.prev_input = 0
    self.prev_output = 0

    # Process each sample 
    for i in range(len(input_signal)):
        # Add resonance effect by mixing in some of the input-output difference
        # This creates emphasis at the cutoff frequency
        resonance_factor = 4.0 * resonance # scale for more noticeable effect
        resonance_input = input_signal[i] + resonance_factor * (input_signal[i] - self.prev_input)

        #Calculate filtered sample