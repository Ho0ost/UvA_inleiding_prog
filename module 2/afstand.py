# autor: Joost van Dijk
# program: afstand
# progam calculates the average distance between two random generated coördinates in a 1x1 area

import math
import random

# function to calculate random distances
def vierkant(n):
    # init
    avr_distance = 0
    a = 0
    b = 0
    distance = 0

    # forloop that loops n times (amount of random checks)
    for i in range (0,n):
        # create random x and y coördinates
        x1 = random.random()
        x2 = random.random()
        y1 = random.random()
        y2 = random.random()

        # calculate distance
        if x1 >= x2:
            a = x1-x2
        else:
            a = x2-x1
        if y1 >= y2:
            b = y1-y2
        else:
            b = y2-y1
        # calculate distance via pythagoras and add distance to previously calculated distances
        distance += math.sqrt((a**2)+(b**2))
    # find average distane by dividing the total distance by the amount of random checks
    avr_distance = distance/n

    #return average distance
    return avr_distance

# set ammount of random tries
tries = 100000
print(vierkant(tries))