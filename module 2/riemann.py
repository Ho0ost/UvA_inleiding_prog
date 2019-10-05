# autor: Joost van Dijk
# program: nulpunten
# this program finds the integral of a function using the riemann methode

import numpy as np
import math
import matplotlib.pyplot as plt

def riemann(func,b,a,n):
    # init
    delta_x = (a-b)/n
    ans = 0
    x_values = []
    y_values = []

    # add starting values (x,y) to list
    x_values.append(b)
    y_values.append(func(b))

    # first step of integral
    for i in np.arange ((b+delta_x),a,delta_x):
        ans += func(i)
        # add x and y values to list for plot
        x_values.append(i)
        y_values.append(func(i))
    ans = delta_x*ans

    # second step of integral
    ans += ((delta_x/2) * (func(b)+func(a)))

    # add last values (x,y) to list
    x_values.append(a)
    y_values.append(func(a))

    # create plot
    plt.plot(x_values, y_values, 'b-')
    plt.show()

    return ans

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

# print results
print ("De integraal van x^2 geeft:")
print (riemann (functie1, 0, 1, 100000))
print ("De integraal van x^(x+0.5) geeft:")
print (riemann (functie2, 0, 1, 100000))
print ("De integraal van sin(x) geeft:")
print (riemann (functie3, 0, math.pi, 100000))
print ("De integraal van tna(cos(sin(x))) geeft:")
print (riemann (functie4, 0.2, 2.2, 100000))
print ("De integraal van sin(x^2) geeft:")
print (riemann (functie5, 0, math.pi, 100000))

