# autor: Joost van Dijk
# program: histogram
# this program shows the average distribution of 100 random numbers summed

import random
import matplotlib.pyplot as plt

# function that generates 100 random numbers, sums them and repeats the process 10.000 times
def SomRandomGetallen():
    return_list = []
    # loop program 10.000 times
    for y in range (10000):
        randoms = 0
        # sum 100 random numbers
        for i in range(100):
            randoms += random.random()
        return_list.append(randoms)
    # returns findings
    return return_list
    
# init
random_list = []
random_list = SomRandomGetallen()

lowers = 0
highers = 0

# check if number higher than 60 or lower than 40
for i in random_list:
    if (i > 60):
        lowers += 1
    elif (i < 40):
        highers += 1

# print percentage higher than 60 and lower than 40
print ((lowers/10000)*100,"% < 40")
print ((highers/10000)*100,"% > 60")

# print histogram
plt.xlim(30, 70)
plt.hist(random_list, bins=50)
plt.show()
