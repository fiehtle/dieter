# Digital Moog Mavis-Style Synthesizer

A digital recreation of the Moog Mavis synthesizer as a VST/AU plugin, built from first principles. This project implements a fully-featured digital synthesizer with modular patching capabilities, developed first in Python for learning and prototyping, then implemented in C++/JUCE for the final plugin.

## Project Structure
```
.
├── python/           # Python prototyping phase
│   ├── src/         # Source code for synth modules
│   ├── tests/       # Unit tests
│   └── examples/    # Example scripts and demonstrations
├── cpp/             # C++/JUCE implementation
│   ├── src/         # Source files
│   ├── include/     # Header files
│   └── tests/       # Unit tests
```

## Features
- VCO (Voltage Controlled Oscillator)
- VCF (Voltage Controlled Filter)
- VCA (Voltage Controlled Amplifier)
- LFO (Low Frequency Oscillator)
- ADSR Envelope Generator
- Virtual patch points
- Clean, minimalist UI inspired by Dieter Rams design principles

## Development Phases
1. Python Prototyping
   - Learning and implementing core DSP concepts
   - Real-time audio testing
   - Visual feedback and analysis

2. C++/JUCE Implementation
   - Professional plugin development
   - DAW integration
   - UI/UX implementation

## Setup
Detailed setup instructions will be added as the project progresses.

## License
TBD 