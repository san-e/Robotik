import RPi.GPIO as GPIO
import time
import signal
import sys
import os

def gracefulExit(sig, frame) -> None:
    os.write(sys.stdout.fileno(), b"\nexiting cleanly\n")
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, gracefulExit)


class LEDController:
    def __init__(self, pins: list, timeout: float) -> None:
        self.pins = pins
        self.timeout = timeout
        GPIO.setmode(GPIO.BOARD)
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

    def blinken(self, anzahl = 1) -> None:
        for _ in range(anzahl):
            for pin in self.pins:
                GPIO.output(pin, True)
            time.sleep(self.timeout)
            for pin in self.pins:
                GPIO.output(pin, False)
            time.sleep(self.timeout)

    def obenNachUnten(self) -> None:
        for pin in self.pins:
            GPIO.output(pin, True)
            time.sleep(self.timeout)

        for pin in self.pins:
            GPIO.output(pin, False)
            time.sleep(self.timeout)

    def untenNachOben(self) -> None:
        pins_rückwarts = list(reversed(self.pins))
        for pin in pins_rückwarts:
            GPIO.output(pin, True)
            time.sleep(self.timeout)

        for pin in pins_rückwarts:
            GPIO.output(pin, False)
            time.sleep(self.timeout)


    def mitteNachAußen(self) -> None:
        pins = self.pins
        assert len(pins) % 2 != 0

        mitte = len(pins) // 2
        pinsLinks = list(reversed(pins[:mitte]))
        pinsRechts = pins[mitte+1:]

        GPIO.output(pins[mitte], True)
        time.sleep(self.timeout)

        for i in range(len(pinsLinks)):
            GPIO.output(pinsLinks[i], True)
            GPIO.output(pinsRechts[i], True)
            time.sleep(self.timeout)

        GPIO.output(pins[mitte], False)
        time.sleep(self.timeout)

        for i in range(len(pinsLinks)):
            GPIO.output(pinsLinks[i], False)
            GPIO.output(pinsRechts[i], False)
            time.sleep(self.timeout)

if __name__ == "__main__":

    pins = [31, 33, 35]
    led = LEDController(pins, 0.1)


    TASTER = 37
    toggled = False
    lastState = False
    GPIO.setup(TASTER, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while True:
        currentState = GPIO.input(TASTER)
        print("toggled: " + str(toggled))
        if lastState == 0 and currentState == 1 and lastState != currentState:
            toggled = not toggled

        if toggled:
            led.mitteNachAußen()
        else:
            pass

        lastState = currentState
