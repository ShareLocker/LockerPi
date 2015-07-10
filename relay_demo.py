import RPi.GPIO
import time
import os
import datetime

##
ROW1 = 2
ROW2 = 2
COL1 = 3

rows = [ROW1, ROW2] #...
cols = [COL1]

RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
RPi.GPIO.setup(ROW1, RPi.GPIO.OUT) # Configure GPIO 2 as output
RPi.GPIO.setup(ROW2, RPi.GPIO.OUT)
RPi.GPIO.setup(COL1, RPi.GPIO.OUT)

def open_location(row, column):
    RPi.GPIO.output(row, False)
    RPi.GPIO.output(column, False)
    time.sleep(3)
    RPi.GPIO.output(row, True)
    RPi.GPIO.output(column, True)

while True:
    for row in rows:
        for col in cols:
            open_location(ROW1, COL1)
            time.sleep(2)
RPi.GPIO.cleanup()
