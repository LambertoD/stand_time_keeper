import RPi.GPIO as GPIO
import sys
import time

channel = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN)

while True:
    if GPIO.input(channel) == GPIO.HIGH:
        print("\nYOU ARE STANDING")
    else:
        print("\nYou are sitting")

    time.sleep(1)

GPIO.cleanup()
