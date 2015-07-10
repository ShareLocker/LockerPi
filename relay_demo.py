import RPi.GPIO
import time
import picamera
import os
import datetime

RPi.GPIO.setmode(RPi.GPIO.BCM)  # Set pin numbering to GPIO, not BOARD pin
RPi.GPIO.setup(2, RPi.GPIO.OUT) # Configure GPIO 2 as output
RPi.GPIO.setup(3, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
 # Configure GPIO 3 as input


camera = picamera.PiCamera()

def check_button():
    if RPi.GPIO.input(3) == RPi.GPIO.LOW:
        print('Say Cheese!')
        os.system("mpg321 -g 300 tng_drawer.mp3 &> /dev/null")
        filename = '{}.jpg'.format(datetime.datetime.now())
        camera.capture(filename)        
        return True
    return False

while True:
    RPi.GPIO.output(2, True)
    time.sleep(1)
    if not check_button():
        RPi.GPIO.output(2, False)
        time.sleep(1)
RPi.GPIO.cleanup()
