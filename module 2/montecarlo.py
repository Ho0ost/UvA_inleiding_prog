# autor: Joost van Dijk
# program: montecarlo
# this program finds integral of a function using the monte carlo methode

import math
import random
import numpy as np
import matplotlib.pyplot as plt

# init functions
def functie1(x):
    return x**2
def functie2(x):
    return x**(x+0.5)
def functie3(x):
    return math.sin(x)
def functie4(x):
    return math.tan(math.cos(math.sin(x)))
def functie5(x):
    return math.sin(x**2)

#generate random number between two variables
def random_num(min,max):
    return min+ (max-min) * random.random()
# find integral
def find_integral(function,lower,upper):
    # find y values for monte carlo range
    y_low,y_high=find_y(function,lower,upper)
    # start monte carlo methode
    integral = montecarlo(function, lower, y_low, upper, y_high)
    print (integral)
# find minimum and maximum y values
def find_y(func,x1,x2):
    y_list = []
    for x in np.arange(x1, x2+0.001, 0.001):
        y = func(x)
        y_list.append(y)
    
    ymin = min(y_list)
    ymax = max(y_list)
    
    if ymin >= 0:
        ymin = 0
    return ymin,ymax
# montecarlo function, used to find integral via monte carlo methode
def montecarlo(func,x1,y1,x2,y2):
    # init
    # lists keep track of random generated coördinates
    random_hit_x_list = []
    random_hit_y_list = []
    random_mis_x_list = []
    random_mis_y_list = []
    # keeps track of hits and misses (on the positive and negative y-ass)
    n_mis = 0
    n_hit = 0
    p_mis = 0
    p_hit = 0
    
    # set amount of random tries, the higher the number, the more accurate, but the slower the program
    random_tries = 100000

    # start montecarlo methode
    for n in range (random_tries):
        # generate random numbers
        random_x = random_num(x1,x2)
        random_y = random_num(y1,y2)
        
        # check if y value is on the positive ass
        if random_y >= 0:
            if random_y <= func(random_x):
                random_hit_x_list.append(random_x)
                random_hit_y_list.append(random_y)
                p_hit += 1
            else:
                random_mis_x_list.append(random_x)
                random_mis_y_list.append(random_y)
                p_mis += 1

        else:
            if random_y >= func(random_x):
                random_hit_x_list.append(random_x)
                random_hit_y_list.append(random_y)
                n_hit += 1
            else:
                random_mis_x_list.append(random_x)
                random_mis_y_list.append(random_y)
                n_mis += 1

    # calculate positive hits ratio
    p_ratio = p_hit/(p_hit+p_mis)
    # if there are hits on the negative y-ass, calculate negative hit ratio
    if (n_hit+n_mis) > 0:
        n_ratio = n_hit/(n_hit+n_mis)

    # calculate integral
    if (n_hit+n_mis) > 0:
        return_integral = (p_ratio*(x2-x1)*(y2-0)) - (n_ratio*(x2-x1)*(0-y1))
    else:
        return_integral = (p_ratio*(x2-x1)*(y2-y1))


    # create plot
    plt.plot(random_hit_x_list, random_hit_y_list, "go",markersize=1)
    plt.plot(random_mis_x_list, random_mis_y_list, "ro",markersize=1)
    plt.show()
    # return integral
    return return_integral

#find interals
find_integral(functie1 ,0 ,1)
find_integral(functie2 ,0 ,1)
find_integral(functie3 ,0 ,math.pi)
find_integral(functie4 ,0.2 ,2.2)
find_integral(functie5 ,0 ,math.pi)

