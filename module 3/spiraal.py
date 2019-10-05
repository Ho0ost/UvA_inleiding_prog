import math
import numpy as np
import matplotlib.pyplot as plt

radius = 0

for alpha in np.arange(0, 20, 0.1):

    radius = 10 - 0.5 * alpha
    x = radius * math.cos(alpha)
    y = radius * math.sin(alpha)

    fig = plt.gcf()
    fig.set_size_inches(5,5)
    plt.plot(x, y, 'bo', markersize = 10) 
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.draw()          
    plt.pause(0.1)
    #plt.clf()          
