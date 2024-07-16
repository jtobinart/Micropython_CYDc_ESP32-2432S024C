# MicroPython_CYDc_ESP32-2432S024C
![labeled image of front side of ESP32-2432S024C](/images/Front_Labeled_ESP32-2432S024C.PNG)
![labeled image of rear side of ESP32-2432S024C](/images/Rear_Labeled_ESP32-2432S024C.PNG)
This is a higher-level library to allow MicroPython users to easily control the ESP32-2432S024C, a smaller version of the Cheap Yellow Display (CYD) but with capacitive (c) touch. Let's call it CYDc. This device uses the cst820 capacitive touch driver chip. Little documentation is available online about the cst820. Advance gesture recognition, pressure measurements, and interrupt pin on the cst820 are nonfunctioning. You can easily capture one and two-finger taps and long presses. Two-finger taps and presses work best when fingers are far apart.


## Dependencies
This library depends on:
* [MicroPython](https://micropython.org/download/ESP32_GENERIC/) - Firmware: v1.23.0 (2024-06-02) .bin (UPDATED)
* [rdagger/micropython-ili9341](https://github.com/rdagger/micropython-ili9341/) - Retrieved: 12/2/23

A copy of rdagger's ili9341 library is available in the _resources_ folder.


## Installation
Follow MicroPython's [installation instructions](https://micropython.org/download/ESP32_GENERIC/) to get your CYDc board ready. Use your preferred MicroPython IDE (e.g. [Thonny](https://thonny.org/)) to transfer CYDc.py and ili9341.py to your CYDc board.


## Usage
You can create a new main.py file and use:
```python
from cydc import CYD
cyd = CYD()
```
or
```python
from cydc import CYD
cyd = CYD(rgb_pmw=False, speaker_gain=512,
          display_width=240, display_height=320,
          wifi_ssid = None, wifi_password = None)
```
to access the CYDc or you can use one of the example programs provided in the repository. You can use the touch demo to test one and two-finger taps and two-finger long presses.


## License
The repository's code is made available under the terms of the MIT license. Please take a look at license.md for more information.
