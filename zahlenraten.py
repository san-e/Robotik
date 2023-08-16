import random
import time


def computerRät(zufallszahl: int, wartezeit: bool) -> None:
    runden: int = 0
    lowerBound: int = 0
    upperBound: int = 100
    while True:
        print("Computer rät...")
        guess: int = random.randint(lowerBound, upperBound)
        if wartezeit:
            time.sleep(random.randint(1, 3))
        
        print(f"Computer rät {guess}.", end=" ")
        if guess == zufallszahl:
            print(f"Das war richtig!\nEs wurden {runden} Runden gespielt")
            break
        elif guess > zufallszahl:
            print("Das war zu hoch.")
            upperBound = guess - 1
        else:
            print("Das war zu niedrig.")
            lowerBound = guess + 1

        runden += 1
            
        

def spielerRät() -> None:
    zufallszahl: int = random.randint(1, 100)
    runden: int = 0
    while True:
        gerateneZahl: int = int(input("Rate eine Zahl: "))
        if gerateneZahl == zufallszahl:
            print(f"Du hast die Zahl erraten!\nEs wurden {runden} Runden gespielt.")
            break
        elif gerateneZahl > zufallszahl:
            print("Die genannte Zahl ist zu groß.")
        else:
            print("Die geratene Zahl ist zu klein.")

        runden += 1
    

if __name__ == "__main__":
    wahl: str = input("Spielmodi:\n(a) Spieler rät\n(b) Computer rät\n").lower()
    if wahl == "a":
        spielerRät()
    elif wahl == "b":
        computerRät(int(input("Welche Zahl soll erraten werden?: ")), True)
    else:
        pass