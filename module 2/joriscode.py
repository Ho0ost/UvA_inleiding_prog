# Opdracht dag 4
# Joris Burger
#
# deze code plot de gegeven grafiek en benaderd dmv de monte-carlo techniek uitkomst de integraal

# imports
import math
import numpy as np
import matplotlib.pyplot as plt
import random



# functie bepalen
def functie1(x):
    return math.tan(math.cos(math.sin(x)))

def montecarlo(func, x_1, y_1, x_2, y_2):
    
    # lijsten
    x_values = []
    y_values = []
    
    # variabelen
    fgoed = 0
    ffout = 0

    # grafiek aanmaken
    for x in np.arange(x_1, x_2, 0.1):
        y = func(x)
        x_values.append(x)
        y_values.append(y)
    plt.plot(x_values, y_values, 'b-')

    for i in range(0,10000):
        # een random punt in het vierkant maken
        x = random.random()
        random_getal_x = x * (x_2-x_1) + x_1
        y = random.random()
        random_getal_y = y * (y_2-y_1) + y_1
        
        # het random punt groen plotten als het een goed punt is
        if 0 < random_getal_y < func(random_getal_x):
            plt.plot(random_getal_x, random_getal_y, 'go')
            fgoed = fgoed + 1
        elif func(random_getal_x) < random_getal_y < 0:
            plt.plot(random_getal_x, random_getal_y, 'go')
            fgoed = fgoed - 1
        # het random punt rood plotten als het een fout punt is
        else: 
            plt.plot(random_getal_x, random_getal_y, 'ro')
            ffout = ffout + 1

    # de integraal berekenen
    integraal = (fgoed / (10000)) * (x_2 - x_1) * (y_2 - y_1)
    plt.show()
    return integraal

print(montecarlo(functie1, 0.2, 0, 2.2, 2))