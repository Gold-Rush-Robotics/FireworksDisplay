# import the libraries
import RPi.GPIO as GPIO
import os
from time import sleep

GPIO.setmode(GPIO.BCM)

# set the pin numbers to be used from Broadcom chip

ledpin = 4  # assign a variable name to pin 4
pushpin = 2  # assign a variable name to pin 2
GPIO.setup(ledpin, GPIO.OUT)  # set GPIO pin 4 as Output
GPIO.setup(pushpin, GPIO.IN)  # set GPIO pin 2 as Input
GPIO.setmode(GPIO.BCM)

while GPIO.input(pushpin):
    sleep(0.2)

os.system('/usr/bin/python3 fireworkDisplay.py')
