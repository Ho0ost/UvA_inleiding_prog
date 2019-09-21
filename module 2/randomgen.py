import random

def random_range(a,b):
    
    return a +(b-a)*random.random()

minimum = -5
maximum = 5
for i in range(10):
    x = random_range(minimum, maximum)
    print(x)