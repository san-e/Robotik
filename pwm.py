import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 29

GPIO.setup(LED, GPIO.OUT)
timeout = 0.001
while True:
    time.sleep(timeout)
    GPIO.output(LED, False)
    time.sleep(timeout)
    GPIO.output(LED, True)
    