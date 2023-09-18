import random
import time


def computerRät(zufallszahl: int, wartezeit: bool) -> None:
    runden = 0
    lowerBound = 0
    upperBound = 100
    while True:
        print("Computer rät...")
        guess = random.randint(lowerBound, upperBound)
        if wartezeit:
            time.sleep(random.randint(1, 3))
        
        print("Computer rät " + str(guess) + ".", end=" ")
        if guess == zufallszahl:
            print("Das war richtig!\nEs wurden " + str(runden) + " Runden gespielt")
            break
        elif guess > zufallszahl:
            print("Das war zu hoch.")
            upperBound = guess - 1
        else:
            print("Das war zu niedrig.")
            lowerBound = guess + 1

        runden += 1
            
        

def spielerRät() -> None:
    zufallszahl = random.randint(1, 100)
    runden = 0
    while True:
        gerateneZahl = int(input("Rate eine Zahl: "))
        if gerateneZahl == zufallszahl:
            print("Du hast die Zahl erraten!\nEs wurden " + str(runden) + " Runden gespielt.")
            break
        elif gerateneZahl > zufallszahl:
            print("Die genannte Zahl ist zu groß.")
        else:
            print("Die geratene Zahl ist zu klein.")

        runden += 1
    

if __name__ == "__main__":
    wahl = input("Spielmodi:\n(a) Spieler rät\n(b) Computer rät\n").lower()
    if wahl == "a":
        spielerRät()
    elif wahl == "b":
        computerRät(int(input("Welche Zahl soll erraten werden?: ")), True)
    else:
        pass