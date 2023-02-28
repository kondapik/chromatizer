# Chromatizer

![Chromatizer App](/chromatizer.png)

Chromatizer enables you to visualize music in realtime using python, a ESP8266 or Raspberry Pi and WS28xx addressable LEDs. This is a personal project inspired by [Scott Lawson's Audio reactive LED strip](https://github.com/scottlawsonbc/audio-reactive-led-strip), to explore the intersection of music and technology.

![Chromatizer App](/LEDControl.png)

## Features

1. Ausio signal processing using Librosa module.
2. UI with customization options and preferences for behavior parameters.
3. User preferences are saved and restored every session.
4. 'Strip'saver to display patterns in case of no audio input.
5. Minimum gain threshold is implemented to distinguish audio signal from noise.
6. Web UI is added by designing UI using PySimpleGUI.

## Installation

1. Python code requires, PySimpleGUI, numpy, pyaudio, librosa, scipy and matplotlib libraries. These can be installed using pip or conda. Easy installation mthods with pre compiled binaries will be added soon.
2. Arduino code for ESP8266 to control led strip can be found in [Scott Lawson's Audio reactive LED strip repository.](https://github.com/scottlawsonbc/audio-reactive-led-strip)
