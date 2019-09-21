# autor: Joost van Dijk
# program: randomwiskunde
# 

import random

# define randomwiskunde function
def randomwiskunde():
    tries = 0
    x = 0
    # loop till number bigger than 1
    while (x < 1):
        x += random.random()
        tries +=1
    # return tries
    return tries

# init
n = 1000000                     # amount of random checks
throws = 0
# find average throws for n tries
for i in range (0,n):
    throws += randomwiskunde()
# print average throws
print("Het gemiddeld aantal worpen (op basis van 1 miljoen trials) is:", round((throws/n),4))