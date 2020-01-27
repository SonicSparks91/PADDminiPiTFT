import digitalio
import board
 
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
 
# Configuration for CS and DC pins for Raspberry Pi
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000   # The pi can be very fast!

backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()
 
# Main loop:
while True:
    if buttonA.value and buttonB.value:
        backlight.value = False              # turn off backlight
    else:
        backlight.value = True               # turn on backlight