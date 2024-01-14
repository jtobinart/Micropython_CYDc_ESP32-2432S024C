# MicroPython_CYDc_ESP32-2432S024C
This is a higher-level library to allow MicroPython users to easily control the ESP32-2432S024C, more commonly known as the smaller Cheap Yellow Device (CYD) with Capacitive (c) Touch (CYDc) This device uses the TFT ili9341 driver chip and cst820 touch driver chip. Little documentation is available online about the cst820. Advance gesture recognition, pressure measurements, and interrupt pin on the cst820 are nonfunctioning. You can easily capture one and two-finger taps and long presses. Two-finger taps and presses work best when fingers are far apart.

## Dependencies
This library depends on:
* [MicroPython](https://micropython.org/download/ESP32_GENERIC/) Firmware: v1.22.1 (2024-01-05) .bin
* [rdagger/micropython-ili9341](https://github.com/rdagger/micropython-ili9341/) Retrieved: 12/2/23

A copy of rdagger's ili9341 library is available in the lib folder.

## Instalations

## Usage
You can create a new main.py file and use:
```python
from cydc import CYDC
cyd = CYDC()
```
to access the CYDc or you can use one of the example programs provided in the repository. You can use the touch demo to test one and two-finger taps and two-finger long presses.

## License
The repository's code is made available under the terms of the MIT license. Please take a look at license.md for more information.
