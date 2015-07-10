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

rowl = [6, 13, 19, 26]
coll = [16, 20]

RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
#RPi.GPIO.setup(ROW1, RPi.GPIO.OUT) # Configure GPIO 2 as output
#RPi.GPIO.setup(ROW2, RPi.GPIO.OUT)
#RPi.GPIO.setup(COL1, RPi.GPIO.OUT)

for r in range(4):
    RPi.GPIO.setup(rowl[r], RPi.GPIO.OUT)
    
for c in range(2):
    RPi.GPIO.setup(coll[c], RPi.GPIO.OUT)

def open_location(row, column):
    row_GPIO = rowl[row]
    col_GPIO = coll[column]
    RPi.GPIO.output(row_GPIO, False)
    RPi.GPIO.output(col_GPIO, False)
    time.sleep(3)
    RPi.GPIO.output(row_GPIO, True)
    RPi.GPIO.output(col_GPIO, True)

while True:
    for r in range(4):
        for c in range(2):
            open_location(r, c)
            time.sleep(0.5)
#    for row in rows:
#        for col in cols:
#            open_location(ROW1, COL1)
#            time.sleep(2)
RPi.GPIO.cleanup()
