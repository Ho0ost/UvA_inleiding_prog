# autor: Joost van Dijk
# program: afstand
# 

import math
import random

def vierkant(n):
    avr_distance = 0
    a = 0
    b = 0
    distance = 0

    for i in range (0,n):
        x1 = random.random()
        x2 = random.random()
        y1 = random.random()
        y2 = random.random()

        if x1 >= x2:
            a = x1-x2
        else:
            a = x2-x1
        if y1 >= y2:
            b = y1-y2
        else:
            b = y2-y1
        distance += math.sqrt((a**2)+(b**2))

    avr_distance = distance/n

    return avr_distance

tries = 1000
print(vierkant(tries))