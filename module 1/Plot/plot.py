import numpy as np
import math
import matplotlib.pyplot as plt

x_values = []
y_values = []
lowest_y = 100
lowest_x = 0

for x in np.arange(0, 1.5, 0.01):
    y = pow(x,x)

    x_values.append(x)
    y_values.append(y)

minposition = y_values.index(min(y_values))

lowest_y = round((y_values[minposition]),2)
lowest_x = round((x_values[minposition]),2)

plt.plot(x_values, y_values, 'b-')
plt.plot(lowest_x, lowest_y, 'ro')
plt.text(0.1,1.20, "(xmin, ymin) = (%s,%s)"%(lowest_x,lowest_y), color = 'black', fontsize = 15)
plt.show()

print(lowest_x,lowest_y)




