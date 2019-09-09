# import random functions, gives a bunch of warnings, but should be fine
from random import randint
import os                           # import for clear screen command

# function to generate prime list
def make_prime_list():
    primelist_return = []                                     # make list to store primes
    num = 2                                            # start at 2 because everything below 2 aint no prime
    dotcnt = 0
    for x in range (5000):                       # find all primes under 10000, loops 5000 times because we skip even numbers      
        Prime = True                                   # make sure prime is set to true else it wont detect primes

        for x in range (2, num):                       # forloop to check for pime, starts at 2 (because everything is divisible by 1) and ends 1 before the input number (num)  
            result = num%x                             # uses modulus to check if result is whole number
            if result == 0:                            # if output from modulus is 0, it is no prime
                Prime = False                          # set prime to false
        if Prime == True:                              # if prime wasn't set to false in the for loop, this means the number is a prime
            primelist_return.append(num)                      # add number to Primelist
            dotcnt +=1
            # update dots for progress feedback
            if (dotcnt == 40):
                os.system("cls")
                print("generating prime list .", end= "")
            if (dotcnt == 80):
                os.system("cls")
                print("generating prime list ..", end= "")
            if (dotcnt == 160):
                os.system("cls")
                print("generating prime list ...", end= "") 
                dotcnt = 0               
            
        if num >=3:                                    # skip even numbers
            num +=2                             
        else:                                          # but dont skip 2
            num +=1         

    return(primelist_return)
# function to find prime factors
def prime_factors(input_value,primelist):
    # init
    NOT_ONE = True
    n=2
    prime_factor_list = []                                  # create list for prime factors
    while(NOT_ONE):
        if (input_value%n == 0):                            # check if division gives whole number
            division_ans = input_value / n                  # run division
            if (division_ans == 1):                         # if division_ans is 1, this means that it is only dividable by itself and therefore it a prime and the last factor
                NOT_ONE = False                             # end while loop
                prime_factor_list.append(input_value)       # add last prime factor to list
            elif division_ans in primelist:                 # if factor is in prime list
                prime_factor_list.append(division_ans)      # add factor to prime_factor_list
                input_value = input_value / division_ans    # set input value to find next factor
                n=1                                         # reset n to start searching for factors (n=1, because it will be set to 2 in next line)
        n +=1                                               # n++
    return (prime_factor_list)                              # return prime factor list
# function to request user input "CURRENTLY NOT USED"
def request_input():
    input_value = int(input(""))
    # incorrect input value
    while (input_value <=1):
        print("invalid input, please try again")
        input_value = int(input("insert value\n"))
    # input value is already prime
    while (input_value in primelist):
        print("number is already a prime, please try again")
        input_value = int(input("insert value\n"))
    return input_value                                          # return input value
# function to find common dividers
def dividers(list1,list2):
    # init
    pos1 = 0
    len1 = len(list1)               # find lenght of list
    while(pos1 < len1):
        if (list1[pos1] in list2):  # check if common divider is found
            return True             # return true
        else:
            pos1 += 1               # else check next pos
# function to calculate riemann zeta
def riemann_zeta(n):
    # init
    riemann = 0
    checks = 1000000                        # ammount of checks, should be infinit, but thats impossible, so 1 million should be fine
    # calculate riemann zeta function
    for x in range (1,checks):              
        riemann = riemann + (1/pow(x,n))
    return (1/riemann)                      # return 1/(riemann zeta function)
# progress function
def progress_bar(percentage):
    print("progress:")
    print("[", end="")
    for z in range (100):
        if (percentage > 0):
            print("|",end="")
        if (percentage <= 0):
            print(" ",end="")
        percentage -= 1
    print("]")



# init
div = 0                     # ammount of dividers found
nodiv = 0                   # ammount of non dividers found
random_checks = 10000       # this gives the amount of random checks, more checks is more accurate, but is more time consuming
last_update = 0

# Generate prime list
print("generating prime list", end= "")
primelist = make_prime_list()          
print("list generated")

for x in range (random_checks):

    # generate random values between (10.000 and 100.000)
    first_value = randint(10000, 100000)
    second_value = randint(10000, 100000)

    # Find prime factors of random values
    prime_factor_list_first = prime_factors(first_value, primelist)
    prime_factor_list_second = prime_factors(second_value, primelist)

    # check for common dividers
    if (dividers(prime_factor_list_first, prime_factor_list_second)):   #check for dividers in dividers function
        # common divider found
        div +=1

    else:
        # no common divider
        nodiv += 1
    # print progress
    
    # update progress
    if (last_update != round(((x/random_checks)*100))):
        os.system("cls")
        progress_bar(round(((x/random_checks)*100)))
        #print("progress: ",round(((x/random_checks)*100)),"%")
    last_update = round(((x/random_checks)*100))

# print results
print ("dividers: ",div)
print ("no dividers: ", nodiv)
print ("chance of no common dividers, Python's prediction:   ", round((nodiv/(random_checks-1)),3))     # Python's results
print ("chance of no common dividers, Riemann's predicition: s", round(riemann_zeta(2),3))               # Riemann's results