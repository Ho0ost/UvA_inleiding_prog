# autor: Joost van Dijk
# program: fractal
# this program generates the mandelbrot set

import math
import numpy as np
import matplotlib.pyplot as plt
import cmath 
import os
  
# function to calculate fractial
def mandel(z, z_zero):
    return z**2 + z_zero
# function to check if value diverges or converges
def converge (z_zero):
    z_new = z_zero
    for i in range (100):
        z_new = mandel(z_new,z_zero)
        # if value diverges, return false
        if z_new.real < -2 or z_new.real > 1 or z_new.imag < -1.5 or z_new.imag > 1.5:
            return False, 0
    # if value didnt diverge after 10 tries, it converges, so return true
    return True

# list to store mandelbrot coordinates
real_conv_list = []
imag_conv_list = []
real_div_list = []
imag_div_list = []

# init starting values
x = -2
y = -1.5
# ints to track progress
cnt = 0
progress = 0

# counter for the real ass (x-ass)
for real_count in range (500):
    cnt += 1
    # counter for the imaginairy ass (y-ass)
    for complex_count in range (500):
        z = complex(x,y)
        # check if value converges
        convergerend = converge(z)
        if (convergerend == True):
            real_conv_list.append(z.real)
            imag_conv_list.append(z.imag)
        else:
            real_div_list.append(z.real)
            imag_div_list.append(z.imag)
        y = y + 0.006
    y = -1.5
    x = x + 0.006
    
    # show progress
    if cnt >= 5:
        progress +=1
        os.system("cls")
        print ("generating mandelbrot",progress,"%")
        cnt = 0

# import values to plot
plt.plot(real_conv_list, imag_conv_list, "bo",markersize=1)
plt.plot(real_div_list, imag_div_list, "wo",markersize=1)
# give plot dimensions
plt.xlim(-2, 1)
plt.ylim(-1.5, 1.5)
# draw plot
plt.show()


