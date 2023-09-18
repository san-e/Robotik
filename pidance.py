# Importieren der benötigten Module
from RPi import GPIO as IO
import random
import time

class LEDController:
    def __init__(self, pins: list, timeout: float) -> None:
        self.pins = pins
        self.timeout = timeout
        IO.setmode(IO.BOARD)
        for pin in pins:
            IO.setup(pin, IO.OUT)
            IO.output(pin, False)

    def blinken(self, anzahl = 1) -> None:
        for _ in range(anzahl):
            for pin in self.pins:
                IO.output(pin, True)
            time.sleep(self.timeout)
            for pin in self.pins:
                IO.output(pin, False)
            time.sleep(self.timeout)

    def obenNachUnten(self) -> None:
        for pin in self.pins:
            IO.output(pin, True)
            time.sleep(self.timeout)

        for pin in self.pins:
            IO.output(pin, False)
            time.sleep(self.timeout)

    def untenNachOben(self) -> None:
        pins_rückwarts = list(reversed(self.pins))
        for pin in pins_rückwarts:
            IO.output(pin, True)
            time.sleep(self.timeout)

        for pin in pins_rückwarts:
            IO.output(pin, False)
            time.sleep(self.timeout)


    def mitteNachAußen(self) -> None:
        pins = self.pins
        assert len(pins) % 2 != 0

        mitte = len(pins) // 2
        pinsLinks = list(reversed(pins[:mitte]))
        pinsRechts = pins[mitte+1:]

        IO.output(pins[mitte], True)
        time.sleep(self.timeout)

        for i in range(len(pinsLinks)):
            IO.output(pinsLinks[i], True)
            IO.output(pinsRechts[i], True)
            time.sleep(self.timeout)

        IO.output(pins[mitte], False)
        time.sleep(self.timeout)

        for i in range(len(pinsLinks)):
            IO.output(pinsLinks[i], False)
            IO.output(pinsRechts[i], False)
            time.sleep(self.timeout)

# Boilerplate-Code, um sicherzustellen, dass das Programm sauber beendet wird, wenn CTRL + C gedrückt wird
import signal
import sys
import os

# Die Funktion gracefulExit wird aufgerufen, wenn das Programm durch CTRL + C beendet wird
def gracefulExit(sig, frame) -> None:
    os.write(sys.stdout.fileno(), b"\nexiting cleanly\n")
    IO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, gracefulExit)  # Registriere die Funktion gracefulExit für das SIGINT-Signal (CTRL + C)

# Mehr Boilerplate-Code für die GPIO-Konfiguration
IO.setwarnings(False)
IO.setmode(IO.BOARD)

# Definition von TASTER und LED Pins
TASTER = [36, 38, 40]
LEDS = [31, 33, 35]

# Sicherstellen, dass gleich viele LEDs und Taster vorhanden sind
assert len(TASTER) == len(LEDS)

ledController = LEDController(pins=LEDS, timeout=0.1)

# Konfiguration der GPIO-Pins für Taster und LEDs
for taste, led in zip(TASTER, LEDS):
    IO.setup(taste, IO.IN, pull_up_down=IO.PUD_DOWN)  # Taster als Eingang konfigurieren, mit Pull-Down-Widerstand
    IO.setup(led, IO.OUT)  # LEDs als Output konfigurieren

# Funktion zur Überprüfung des Tasterdrucks
def pollButtons() -> int:
    pressed = False

    # Solange kein Taster gedrückt wurde...
    while not pressed:
        # Iteriere über jeden Taster und überprüfe, ob dieser gedrückt ist.
        for buttonIndex, taste in enumerate(TASTER):
            if IO.input(taste):
                pressed = True
                break

    # Warten, bis der Taster losgelassen wurde
    while IO.input(TASTER[buttonIndex]):
        pass

    time.sleep(0.2)
    return buttonIndex

# Funktion zum Umschalten der Zustände der LEDs
def toggleLed(pin) -> None:
    IO.output(pin, not IO.input(pin))

# Einstellungen für das Spiel
RUNDEN = 7
reihenfolge = [random.randint(0, 2) for _ in range(RUNDEN)]  # Zufällige Reihenfolge von Tasten für jede Runde
CHEATS = True  # Wenn True, wird die Reihenfolge während des Spiels angezeigt

# Hauptschleife - einmal pro Runde
for runde in range(RUNDEN):
    # Die Reihenfolge für diese Runde
    dieseRunde = reihenfolge[:runde + 1]

    # LEDs blinken lassen
    for led in dieseRunde:
        IO.output(LEDS[led], True)  # LED einschalten
        time.sleep(0.5)  # 0,5 Sekunden warten
        IO.output(LEDS[led], False)  # LED ausschalten
        time.sleep(0.5)  # 0,5 Sekunden warten

    for led in dieseRunde:
        if CHEATS: print(led, end="\r")  # Wenn Cheats aktiviert sind, gib die aktuelle LED aus
        buttonIndex = pollButtons()  # Überwache den Tasterdruck

        # Falls der falsche Taster gedrückt wird, verliert man
        if buttonIndex != led:
            print("Falsch! Du hast Taster " + str(buttonIndex) + " anstatt Taster " + str(led) + " gedrückt!\nDie Reihenfolge war " + str(reihenfolge))
            ledController.blinken(5)  # LEDS 5 mal blinken lassen
            IO.cleanup()
            sys.exit(0)  # Terminieren

# Wenn man nicht vorher verloren hat, hat man gewonnen
ledController.mitteNachAußen()
IO.cleanup()
