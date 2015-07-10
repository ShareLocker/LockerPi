import RPi.GPIO
import time
import os
import datetime

RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
RPi.GPIO.setup(2, RPi.GPIO.OUT) # Configure GPIO 2 as output

while True:
    RPi.GPIO.output(2, True)
    time.sleep(1)
    RPi.GPIO.output(2, False
    time.sleep(1)
RPi.GPIO.cleanup()
