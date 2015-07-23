import RPi.GPIO
import time
import os
import datetime
import requests

# hardware configuration
Nrow = 4
Ncol = 2
secret = "1"
#host_ip = "https://sharelockers.localtunnel.me"
host_ip = "http://www.sharelockers.com"
connect = host_ip + '/hubs/connected/' + secret
poll = host_ip + '/hubs/poll/' + secret
finished = host_ip + '/hubs/finished/' + secret
failed = host_ip + '/hubs/failed/' + secret
rowl = [6, 13, 19, 26]
coll = [16, 20]

# behavior configuration
open_time = 1 # open the latch for ... seconds
poll_time = 0.5#2

# begin setup code
def PiPinSetup(initial=False):
    RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
    for pin in rowl + coll:
        RPi.GPIO.setup(pin, RPi.GPIO.OUT)
        if initial:
            RPi.GPIO.output(pin, True)


PiPinSetup(initial=True)
RPi.GPIO.cleanup()
try:
    resp = requests.get(connect)
except:
    print('Cannot connect right now, will try again shortly.')
# functions for continuous polling operation
def poll_status():
    try:
        resp = requests.get(poll)
    except:
        print('Cannot connect right now, will try again shortly.')
    action, col, row = tuple(char for char in resp.text)[:3]
    return action, col, row


def open_location(column, row):
    try:
        row_GPIO = rowl[row-1]
        col_GPIO = coll[column-1]
        RPi.GPIO.output(row_GPIO, False)
        RPi.GPIO.output(col_GPIO, False)
        time.sleep(open_time)
        RPi.GPIO.output(row_GPIO, True)
        RPi.GPIO.output(col_GPIO, True)
    except IndexError:
        resp = requests.get(failed) # FIXME: add views in Django to correspond to this
# constant loop
while True:
    action, col, row = poll_status()
    print(action, col, row)
    if action == "?":
        print('Opening a locker', col, row)
        PiPinSetup()
        open_location(int(col), int(row))
        RPi.GPIO.cleanup()
        time.sleep(open_time)
        resp = requests.get(finished)
        os.system('espeak "Thank you for using ShareLocker. Have a nice day!"')
    time.sleep(poll_time)
