from RaspberryPi import raspiLedMethods as Methods
#import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)


led = Methods.LedControl()


while True:

    is_night_now = led.on_or_off()

    if is_night_now:

        GPIO.output(21, GPIO.HIGH)
    else:
        GPIO.output(21, GPIO.LOW)

    sleep(60)



