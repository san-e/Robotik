# Ein Programm zur Berechnung des größten gemeinsamen Teilers (ggT) zweier Zahlen
# (c) Tim Julian Jarzev
#

import random

# Subtraktionsmethode
def ggT_s(a: int, b: int) -> int:
    if b > a: a, b = b, a
    
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a
    if b == 0:
        return a
    else:
        return b
        
# Divisionsmethode
def ggT_d(a: int, b: int) -> int:
    if b > a: a, b = b, a
    rest = 1
    while rest > 0:
        rest = a % b
        a = b
        b = rest
        
    return a
    
    

in0 = int(input("Zahl 1: "))
in1 = int(input("Zahl 2: "))
print("ggT: " + str(ggT_d(in0, in1)))