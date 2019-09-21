# autor: Joost van Dijk
# program: twitter ei
# program is used to estimate area of the twitter egg

# imports
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import os     

# function for the egg
def egg(x,y):
    return math.sqrt(x**2+y**2)+((2/3)*math.sqrt(x**2+((5/6)-y)**2))

#generate random number between two variables
def random_num(min,max):
    return min+ (max-min) * random.random()
    
# montecarlo function, used to find integral via monte carlo methode
def montecarlo(random_tries):
    # lists with x and y coördinates
    random_hit_x_list = []
    random_hit_y_list = []
    random_mis_x_list = []
    random_mis_y_list = []
    # keeps track of hits and misses
    mis = 0
    hit = 0
    # cnt is used to update estimated area after every 1000 checks
    cnt = 0
    guesses = 0

    # start forloop to generate, check and place random coördinates
    for n in range (random_tries):

        cnt += 1    
        # generate random point
        random_x = random_num(-1,1)
        random_y = random_num(-0.4,1.4)
        
        # if point is in the egg, add to hit list, else add to mis list
        if egg(random_x,random_y) <= 1:
            random_hit_x_list.append(random_x)
            random_hit_y_list.append(random_y)
            hit += 1
        else:
            random_mis_x_list.append(random_x)
            random_mis_y_list.append(random_y)
            mis += 1

        # update estimated area after every 1000 checks
        if cnt >= 1000:
            guesses += 1000
            opp = (hit/mis)
            os.system("cls")
            print("estimated area after",guesses,"random points:", round((opp),3))
            cnt = 0

    
    print("total hits:", hit)
    print("total misses:", mis)

    # create plot
    plt.plot(random_hit_x_list, random_hit_y_list, "wo",markersize=1)
    plt.plot(random_mis_x_list, random_mis_y_list, "bo",markersize=1)
    plt.show()
    
    return 

# argument gives amount of random points
montecarlo(1000000)
