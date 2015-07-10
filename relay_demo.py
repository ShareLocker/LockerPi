import RPi.GPIO
import time
import os
import datetime
import requests

# hardware configuration
Nrow = 4
Ncol = 2
secret = "2"
host_ip = "https://sharelockers.localtunnel.me"
connect = host_ip + '/hubs/connected/' + secret
poll = host_ip + '/hubs/poll/' + secret
finished = host_ip + '/hubs/finished/' + secret
rowl = [6, 13, 19, 26]
coll = [16, 20]

# behavior configuration
open_time = 3 # open the latch for ... seconds
poll_time = 2

    # begin setup code
def PiPinSetup():
    RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
    for r in range(4): # configure the row output pins
        RPi.GPIO.setup(rowl[r], RPi.GPIO.OUT)
    for c in range(2): # configure the column output pins
        RPi.GPIO.setup(coll[c], RPi.GPIO.OUT)

resp = requests.get(connect)

# functions for continuous polling operation
def poll_status():
    resp = requests.get(poll)
    action, col, row = tuple(char for char in resp.text)[:3]
    return action, col, row


def open_location(column, row):
    row_GPIO = rowl[row]
    col_GPIO = coll[column]
    RPi.GPIO.output(row_GPIO, False)
    RPi.GPIO.output(col_GPIO, False)
    time.sleep(3)
    RPi.GPIO.output(row_GPIO, True)
    RPi.GPIO.output(col_GPIO, True)



#while True:
#for k in range(1):
#    for r in range(4):
#        for c in range(2):
#            open_location(r, c)
#            time.sleep(0.5)
#    for row in rows:
#        for col in cols:
#            open_location(ROW1, COL1)
#            time.sleep(2)

# constant loop
while True:
    action, col, row = poll_status()
    if action == "?":
        PiPinSetup()
        open_location(col, row)
        RPi.GPIO.cleanup()
        time.sleep(open_time)
    else:
        time.sleep(poll_time)
