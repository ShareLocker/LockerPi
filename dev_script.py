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
def PiPinSetup(initial=False):
    RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
	for pin in rowl + coll:
        RPi.GPIO.setup(pin, RPi.GPIO.OUT)
		if initial:
			RPi.GPIO.output(pin, True)


PiPinSetup(initial=True)
RPi.GPIO.cleanup()
resp = requests.get(connect)

# functions for continuous polling operation
def poll_status():
    resp = requests.get(poll)
    action, col, row = tuple(char for char in resp.text)[:3]
    return action, col, row


def open_location(column, row):
    row_GPIO = rowl[row-1]
    col_GPIO = coll[column-1]
    RPi.GPIO.output(row_GPIO, False)
    RPi.GPIO.output(col_GPIO, False)
    time.sleep(open_time)
    RPi.GPIO.output(row_GPIO, True)
    RPi.GPIO.output(col_GPIO, True)

# constant loop
while True:
    action, col, row = poll_status()
    if action == "?":
        PiPinSetup()
        open_location(col, row)
        RPi.GPIO.cleanup()
        time.sleep(open_time)
        resp = requests.get(finished)
    time.sleep(poll_time)
