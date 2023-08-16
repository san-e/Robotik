import random

randomNumber: int = random.randint(1, 100)

runden: int = 0

while True:
    gerateneZahl: int = int(input("Rate eine Zahl: "))
    if gerateneZahl == randomNumber:
        print(f"Du hast die Zahl erraten!\nEs wurden {runden} Runden gespielt.")
        break
    elif gerateneZahl > randomNumber:
        print("Die genannte Zahl ist zu groß.")
    else:
        print("Die geratene Zahl ist zu klein.")


    runden += 1