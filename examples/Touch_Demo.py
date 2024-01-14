# CYDc Touchscreen Demo
# Tags: Micropython Smaller Cheap Yellow Device Capacitive Touch cst820 DIYmall ESP32-2432S024C 
# Last Updated: Jan. 14, 2024
# Author(s): James Tobin
# License: MIT
# https://github.com/jtobinart/Micropython_CYDc_ESP32-2432S024C

from cydc import CYDC
import time

# Creat an instance of CYDC
cyd = CYDC()

# Draw "TOUCH ME" at top of display.
cyd.display.draw_text8x8(cyd.display.width // 2 - 32, 10, "TOUCH ME", cyd.WHITE, background=cyd.RED)

# List of color choices
colors = [cyd.RED, cyd.GREEN, cyd.BLUE]

c = 0    # Initial color choice
r = 4    # Radius of cirlces

while True:
    time.sleep(0.05)
    fingers, raw_x, raw_y = cyd.touches()
    #print("Touches:", i, x, y)

    if fingers is 0:
        # No Fingers Detected
        longpress_flag = False
        pass
    
    if fingers is 2:
        if longpress_flag == True:
            # Two Finger Long Press Action - Works best When fingers are far apart.
            break
        # Two Finger Tap Action - Works best when fingers are far apart
        longpress_flag = True
        c=(c+1)%len(colors)
        time.sleep(0.1)
        pass
    
    if fingers is 1:
        # One Finger Tap Action
        longpress_flag = False
        # Prevent circles from appearing off screen.
        y = min(max(((cyd.display.height - 1) - raw_y), (r+1)),(cyd.display.height-(r+1)))
        x = min(max(((cyd.display.width - 1) - raw_x), (r+1)),(cyd.display.width-(r+1)))
        # Create circle
        cyd.display.fill_circle(x, y, r, colors[c])

cyd.shutdown()