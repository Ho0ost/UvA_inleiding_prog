# autor: Joost van Dijk
# program: histogram
# 

import random
import matplotlib.pyplot as plt

def SomRandomGetallen():
  
    return_list = []
    for y in range (10000):
        randoms = 0
        for i in range(100):
            randoms += random.random()
        return_list.append(randoms)
    return return_list

    
random_list = []

random_list = SomRandomGetallen()

lowers = 0
highers = 0

for i in random_list:
    if (i > 60):
        lowers += 1
    elif (i < 40):
        highers += 1

print ((lowers/10000)*100,"% < 40")
print ((highers/10000)*100,"% > 60")

plt.xlim(30, 70)
plt.hist(random_list, bins=50)
plt.show()
