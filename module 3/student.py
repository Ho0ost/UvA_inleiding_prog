# autor: Joost van Dijk
# program: 
# 

import math
import random
import numpy as np
import matplotlib.pyplot as plt

def find_delta ():
    alpha = (random.random() * 360)*(math.pi/180)
    d_x = math.cos(alpha)
    d_y = math.sin(alpha)
    return d_x, d_y

delta_x = 0
delta_y = 0
x_red = 0
y_red = 0
x_red_list = [0]
y_red_list = [0]

x_blue = 0
y_blue = 0
x_blue_list = [0]
y_blue_list = [0]
distance_x_list = [0,0]
distance_y_list = [0,0]


for i in np.arange(0, 201, 1):

    # plot grafiek
    plt.plot(x_red_list, y_red_list, 'r-')  
    plt.plot(x_red, y_red, 'ro', markersize = 10)
    plt.plot(x_blue_list, y_blue_list, 'b-') 
    plt.plot(x_blue, y_blue, 'bo', markersize = 10)
    distance_x_list[0] = x_blue
    distance_x_list[1] = x_red
    distance_y_list[0] = y_blue
    distance_y_list[1] = y_red
    plt.plot(distance_x_list, distance_y_list, 'g-')
    plt.text(-18,-18, "%s / 200 steps" %i, color = 'black', fontsize = 15) 
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.draw()          
    plt.pause(0.1)
    plt.clf()           

    delta_x, delta_y = find_delta()
    x_red += delta_x
    x_red_list.append(x_red)
    y_red += delta_y
    y_red_list.append(y_red)

    delta_x, delta_y = find_delta()
    x_blue += delta_x
    x_blue_list.append(x_blue)
    y_blue += delta_y
    y_blue_list.append(y_blue)