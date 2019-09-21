# autor: Joost van Dijk
# program: nulpunten
# this program finds and plots zeropoints of functions

import numpy as np
import math
import matplotlib.pyplot as plt

# define function to find zero values
def nulpunten(a_val,b_val,c_val):
    zeropoints = []                                                     # create empty list
    d_val = b_val**2-4*a_val*c_val                                      # calculate discriminant
    if d_val < 0:                                                       # if discriminant is less than zero, no zero points
        return zeropoints
    elif d_val == 0:                                                    # if discriminant is zero, only one zero point
        first_zero = round(((-b_val)/(2*a_val)),2)
        zeropoints.append (first_zero)
        return zeropoints
    elif d_val > 0:                                                     # if discriminant bigger than zero, multiple zero points
        first_zero = round(((-b_val + math.sqrt(d_val))/(2*a_val)),2)
        second_zero = round(((-b_val - math.sqrt(d_val))/(2*a_val)),2)
        zeropoints.append (first_zero)
        zeropoints.append (second_zero)
        return zeropoints

# init
x_values = []
y_values = []
a = 1
b = 2
c = -10
x_zero_list = []

# find zero points
x_zero_list = nulpunten(a,b,c)

# print zero points
print (x_zero_list)

# create x and y list
for x in np.arange(-6, 6, 0.1):
    y = a*x**2 + b*x + c

    x_values.append(x)
    y_values.append(y)

# only one zero point, plot only one point
if len(x_zero_list) == 1:
    plt.plot(x_zero_list[0], 0, 'ro')
# two zero points, plot two points
elif len(x_zero_list) == 2:
    plt.plot(x_zero_list[0], 0, 'ro')
    plt.plot(x_zero_list[1], 0, 'ro')
# no zero points, dont plot points
elif len(x_zero_list) == 0:
    print("Deze functie heeft geen nulpunten")

# plot function
plt.hlines(0,-6,6,"r", "dotted")
plt.plot(x_values, y_values, 'b-')
plt.axis([-6, 6, -15, 20])
plt.show()