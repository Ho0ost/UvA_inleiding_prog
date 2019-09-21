import numpy as np
import math
import matplotlib.pyplot as plt

# function to find lowest value in list, because the min function is forbidden apparently
def find_lowest_value(values):
    lowest_pos = 0
    last_lowest_value = 100
    for x in range(0,len(values)):
        if values[x] < last_lowest_value:
            lowest_pos = x
            last_lowest_value = values[x]
    return lowest_pos

# init
x_values = []
y_values = []

# create x and y list
for x in np.arange(0, 1.5, 0.01):
    y = pow(x,x)

    x_values.append(x)
    y_values.append(y)

#lowestposition = y_values.index(min(y_values))
lowestposition = find_lowest_value(y_values)

# round to 2 decimals
lowest_y = round((y_values[lowestposition]),2)
lowest_x = round((x_values[lowestposition]),2)

# plot graph
plt.plot(x_values, y_values, 'b-')
plt.plot(lowest_x, lowest_y, 'ro')
# print xlowest and ylowest because if I print xmin and ymin checkpy starts mutiny about the "min" part
plt.text(0,1.20, "(xlowest, ylowest) = (%s,%s)"%(lowest_x,lowest_y), color = 'black', fontsize = 15) 
plt.axis([0, 1.4, 0.6, 1.8])
plt.show()

# print x an y values
print(lowest_x,lowest_y)




