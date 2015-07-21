import RPi.GPIO
import time
import os
import datetime
import requests

# hardware configuration
Nrow = 4
Ncol = 2
rowl = [6, 13, 19, 26]
coll = [16, 20]

# behavior configuration
open_time = 3 # open the latch for ... seconds

# begin setup code
def PiPinSetup(initial=False):
    RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
    for pin in rowl + coll:
        RPi.GPIO.setup(pin, RPi.GPIO.OUT)
        if initial:
            RPi.GPIO.output(pin, True)
            RPi.GPIO.output(pin, False)
            
def open_location(column, row):
    row_GPIO = rowl[row]
    col_GPIO = coll[column]
    RPi.GPIO.output(row_GPIO, False)
    RPi.GPIO.output(col_GPIO, False)
    time.sleep(open_time)
    RPi.GPIO.output(row_GPIO, True)
    RPi.GPIO.output(col_GPIO, True)

PiPinSetup()

for k in range(1): # cycle 2 times
   for r in range(Nrow):
       for c in range(Ncol):
           open_location(c, r)
           time.sleep(0.5)

RPi.GPIO.cleanup()
